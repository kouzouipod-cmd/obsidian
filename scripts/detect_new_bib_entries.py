#!/usr/bin/env python3
"""
Detect new BibTeX entries added in the last 24 hours with abstracts.
Marks entries that already have a note anywhere in the vault (existing_note).
Outputs: new_entries.json (only if new entries found)
"""

import os
import argparse
import json
import subprocess
import re
from pathlib import Path
import bibtexparser
from bibtexparser.bparser import BibTexParser


def get_new_entry_keys():
    """Get BibTeX entry keys added in the last 24 hours via git diff."""
    bib_file = "15_zotero/zotero.bib"

    # Get commits from last 24 hours
    since = "24 hours ago"
    cmd = [
        "git", "log",
        f"--since={since}",
        "--pretty=format:%H",
        "--", bib_file
    ]

    result = subprocess.run(cmd, capture_output=True, text=True)
    commits = result.stdout.strip().split('\n')

    if not commits or commits == ['']:
        print("No commits found in the last 24 hours")
        return set()

    print(f"Found {len(commits)} commit(s) in last 24 hours")

    # Extract new entry keys from diff
    new_entry_keys = set()

    for commit in commits:
        # Get diff for this commit
        diff_cmd = ["git", "diff", f"{commit}^", commit, "--", bib_file]
        try:
            diff_result = subprocess.run(diff_cmd, capture_output=True, text=True, check=True)

            # Parse added lines to find @article{key}, @misc{key}, etc.
            for line in diff_result.stdout.split('\n'):
                if line.startswith('+') and not line.startswith('+++'):
                    # Look for BibTeX entry declarations: @article{key, @misc{key, etc.
                    match = re.match(r'^\+@\w+\{([^,]+)', line)
                    if match:
                        entry_key = match.group(1).strip()
                        new_entry_keys.add(entry_key)
                        print(f"  Found new entry: {entry_key}")

        except subprocess.CalledProcessError as e:
            print(f"Warning: Failed to get diff for commit {commit[:8]}: {e}")
            continue

    print(f"\nTotal new entry keys found: {len(new_entry_keys)}")
    return new_entry_keys


def parse_bibtex_file(bib_file, entry_keys_filter=None, require_abstract=True):
    """Parse BibTeX file and return entries with abstracts, optionally filtered by keys."""

    with open(bib_file, 'r', encoding='utf-8') as f:
        bib_content = f.read()

    parser = BibTexParser(common_strings=True)
    parser.ignore_nonstandard_types = False

    bib_database = bibtexparser.loads(bib_content, parser=parser)

    entries_with_abstract = []

    for entry in bib_database.entries:
        entry_key = entry.get('ID', '')

        # Filter by entry keys if provided
        if entry_keys_filter and entry_key not in entry_keys_filter:
            continue

        # Check if abstract exists and is not empty
        abstract = entry.get('abstract', '').strip()
        if not abstract and require_abstract:
            print(f"Skipping {entry_key}: No abstract")
            continue

        # Extract metadata
        entry_data = {
            'entry_key': entry_key,
            'author': entry.get('author', 'Unknown'),
            'title': entry.get('title', 'Untitled'),
            'journal': entry.get('journal', entry.get('booktitle', 'Unknown')),
            'year': entry.get('year', 'Unknown'),
            'abstract': abstract,
            'doi': entry.get('doi', ''),
            'url': entry.get('url', ''),
            'pmid': entry.get('pmid', ''),
            'volume': entry.get('volume', ''),
            'issue': entry.get('issue', ''),
            'pages': entry.get('pages', ''),
        }

        entries_with_abstract.append(entry_data)

    return entries_with_abstract


SKIP_DIRS = {".git", ".github", ".obsidian", ".trash", "scripts", "90_attachments", "15_zotero"}
CITEKEY_RE = re.compile(r'^citekey:\s*["\']?([^"\'\s]+)["\']?\s*$', re.MULTILINE)


def build_existing_note_index():
    """Map citekey -> existing note path, searching the whole vault.

    Notes made by the local builder (build_vault_notes.ps1) are named
    '@<citekey> <Japanese title>.md' and may live outside 10_article/
    (e.g. 'CAPS freeflap/'). The old check only looked for the exact
    '10_article/@<citekey>.md', so it missed them and this workflow wrote
    a second note for the same paper (2026-09-12, 09-15, 09-16).
    We therefore match by the frontmatter 'citekey:' field, anywhere.
    """
    index = {}
    for path in Path(".").rglob("*.md"):
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        try:
            head = path.read_text(encoding="utf-8", errors="ignore")[:2000]
        except OSError:
            continue
        m = CITEKEY_RE.search(head)
        if m:
            index.setdefault(m.group(1), path.as_posix())
    return index


def note_text_for_infographic(note_path):
    """Abstract substitute taken from the note itself.

    Many Zotero items have no abstract in the bib (CAPS, traumatic neuroma),
    but the builder note carries it in the '> [!Abstract]' callout. If that
    is empty too, fall back to the note's '# 1 AI要約' body.
    """
    text = Path(note_path).read_text(encoding="utf-8", errors="ignore")
    lines = text.split("\n")

    for i, l in enumerate(lines):
        # 古いノートは '>[!Abstract]'（空白なし）で書かれている。空白を仮定すると
        # 抄録を見落とし、代わりにAI要約から画像を作ることになる（Hsiung/Numajiriで発生）。
        if l.strip().replace("> [", ">[").startswith(">[!Abstract]"):
            out = []
            for m in lines[i + 1:]:
                if not m.startswith(">"):
                    break
                out.append(re.sub(r"^>\s?", "", m))
            abstract = " ".join(out).strip()
            if len(abstract) > 100:
                return abstract, "note-abstract"
            break

    try:
        start = next(i for i, l in enumerate(lines) if l.strip() == "# 1 AI要約")
    except StopIteration:
        return "", ""
    body = []
    for m in lines[start + 1:]:
        if m.startswith("# "):
            break
        if "infographic.png" in m:
            continue
        body.append(m)
    summary = "\n".join(body).strip()
    return (summary, "note-summary") if len(summary) > 100 else ("", "")


def backfill(folder, limit):
    """Entries whose note exists but has no infographic yet (manual run)."""
    print("=" * 60)
    print(f"Backfill: notes without infographic (folder='{folder}', limit={limit})")
    print("=" * 60)

    existing = build_existing_note_index()
    targets = {
        k: p for k, p in existing.items()
        if not k.startswith("{{")
        and not p.startswith("99_template")
        and (not folder or p.split("/")[0] == folder)
        and not (Path("90_attachments") / k / "infographic.png").exists()
    }
    print(f"Notes without infographic: {len(targets)}")
    if not targets:
        # 空集合を渡すと parse_bibtex_file の絞り込みが外れて bib 全件になる
        return

    entries = parse_bibtex_file("15_zotero/zotero.bib",
                                entry_keys_filter=set(targets), require_abstract=False)
    out = []
    for e in sorted(entries, key=lambda x: targets[x['entry_key']]):
        e['existing_note'] = targets[e['entry_key']]
        source = "bib"
        if not e['abstract']:
            e['abstract'], source = note_text_for_infographic(e['existing_note'])
        if not e['abstract']:
            print(f"  skip {e['entry_key']}: no abstract or summary anywhere")
            continue
        e['abstract_source'] = source
        out.append(e)
        if len(out) >= limit:
            break

    for e in out:
        print(f"  - {e['entry_key']} [{e['abstract_source']}] -> {e['existing_note']}")
    if out:
        with open('new_entries.json', 'w', encoding='utf-8') as f:
            json.dump(out, f, indent=2, ensure_ascii=False)
    print(f"\nBackfill targets this run: {len(out)} "
          f"(remaining after this run: {len(targets) - len(out)})")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--backfill", action="store_true",
                        help="process existing notes that have no infographic")
    parser.add_argument("--folder", default="",
                        help="backfill only notes in this top-level folder")
    parser.add_argument("--limit", type=int, default=25)
    args = parser.parse_args()
    if args.backfill:
        backfill(args.folder, args.limit)
        return

    print("=" * 60)
    print("Detecting new BibTeX entries (last 24 hours)")
    print("=" * 60)

    # Step 1: Get new entry keys from git diff
    new_entry_keys = get_new_entry_keys()

    if not new_entry_keys:
        print("\n✅ No new entries found in the last 24 hours. Exiting.")
        return

    # Step 2: Parse BibTeX file and filter by new entry keys
    bib_file = "15_zotero/zotero.bib"

    if not os.path.exists(bib_file):
        print(f"ERROR: BibTeX file not found: {bib_file}")
        return

    print(f"\nParsing {bib_file} for new entries...")
    all_new_entries = parse_bibtex_file(bib_file, entry_keys_filter=new_entry_keys)

    print(f"Found {len(all_new_entries)} new entries with abstracts")

    # Step 3: Mark entries that already have a note.
    # They still get an infographic, but the workflow must NOT write a note;
    # embed_infographic.py inserts the image into the existing note instead.
    existing = build_existing_note_index()
    new_entries = []
    for entry in all_new_entries:
        note = existing.get(entry['entry_key'], '')
        entry['existing_note'] = note
        if note:
            print(f"Existing note: {entry['entry_key']} -> {note} (infographic only)")
        new_entries.append(entry)

    print(f"\nEntries to process: {len(new_entries)} "
          f"({sum(1 for e in new_entries if e['existing_note'])} infographic only)")

    # Step 4: Output results
    if new_entries:
        with open('new_entries.json', 'w', encoding='utf-8') as f:
            json.dump(new_entries, f, indent=2, ensure_ascii=False)

        print("\n✅ Created new_entries.json with the following entries:")
        for entry in new_entries:
            print(f"  - {entry['entry_key']}: {entry['author'][:50]} ({entry['year']})")
    else:
        print("\n✅ No new entries to process (all skipped: no abstract or duplicate)")
        # Do NOT create new_entries.json if no new entries


if __name__ == "__main__":
    main()
