#!/usr/bin/env python3
"""
Detect new BibTeX entries added in the last 24 hours with abstracts.
Marks entries that already have a note anywhere in the vault (existing_note).
Outputs: new_entries.json (only if new entries found)
"""

import os
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


def parse_bibtex_file(bib_file, entry_keys_filter=None):
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
        if not abstract:
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


def main():
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
