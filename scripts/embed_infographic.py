#!/usr/bin/env python3
"""
Post-process after the Claude/Gemini step, for entries whose note already
existed (existing_note set by detect_new_bib_entries.py):

1. If the LLM step wrote '10_article/@<key>.md' anyway, remove it.
   Only files that are NOT tracked by git are removed, i.e. files created
   in this run. A committed note is never touched.
2. Insert '![[90_attachments/<key>/infographic.png]]' right after the
   '# 1 AI要約' heading of the existing note, if the image exists and the
   note does not embed it yet. This is the same line build_vault_notes.ps1
   writes, so a later local rebuild produces the identical note.
"""

import json
import subprocess
from pathlib import Path


def is_tracked(path: Path) -> bool:
    r = subprocess.run(["git", "ls-files", "--error-unmatch", path.as_posix()],
                       capture_output=True, text=True)
    return r.returncode == 0


def main():
    if not Path("new_entries.json").exists():
        print("new_entries.json not found; nothing to do")
        return

    entries = json.loads(Path("new_entries.json").read_text(encoding="utf-8"))
    for e in entries:
        key, note = e["entry_key"], e.get("existing_note", "")
        if not note:
            continue

        stray = Path("10_article") / f"@{key}.md"
        if stray.exists() and stray.as_posix() != note and not is_tracked(stray):
            stray.unlink()
            print(f"Removed duplicate written by LLM step: {stray}")

        png = Path("90_attachments") / key / "infographic.png"
        if not png.exists():
            print(f"{key}: no infographic generated; note left unchanged")
            continue

        embed = f"![[90_attachments/{key}/infographic.png]]"
        p = Path(note)
        text = p.read_text(encoding="utf-8")
        if embed in text:
            print(f"{key}: already embedded")
            continue

        lines = text.split("\n")
        idx = next((i for i, l in enumerate(lines) if l.strip() == "# 1 AI要約"), None)
        if idx is None:
            print(f"{key}: '# 1 AI要約' heading not found in {note}; skipped")
            continue
        lines.insert(idx + 1, embed)
        p.write_text("\n".join(lines), encoding="utf-8")
        print(f"{key}: embedded infographic into {note}")


if __name__ == "__main__":
    main()
