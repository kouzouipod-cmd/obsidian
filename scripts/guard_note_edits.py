#!/usr/bin/env python3
"""
Safety net: an existing note may only gain the infographic embed line.

On 2026-09-21 the LLM step rewrote 15 curated notes in
'maxillary reconstruction/' — replacing the summaries and the wikilink
section — although the prompt told it not to write notes at all. Prompts
cannot be relied on for this, so every tracked .md modified during the run
is inspected here: if its diff is anything other than added
'![[90_attachments/<key>/infographic.png]]' lines, the file is restored to
HEAD and the run is failed so the deviation is visible.

New, untracked .md files are left alone (that is the normal path for papers
the user added to Zotero without a note).
"""

import re
import subprocess
import sys

EMBED_RE = re.compile(r"^!\[\[90_attachments/[^\]]+/infographic\.png\]\]$")


def run(*args):
    return subprocess.run(args, capture_output=True, text=True, check=True).stdout


def main():
    changed = [p for p in run("git", "diff", "--name-only", "--", "*.md").splitlines() if p]
    if not changed:
        print("No tracked note was modified.")
        return 0

    reverted = []
    for path in changed:
        diff = run("git", "diff", "--unified=0", "--", path).splitlines()
        offending = []
        for line in diff:
            if line.startswith("+++") or line.startswith("---") or line.startswith("@@"):
                continue
            if line.startswith("-"):
                offending.append(line)
            elif line.startswith("+") and not EMBED_RE.match(line[1:].strip()):
                offending.append(line)
        if offending:
            print(f"UNEXPECTED EDIT in {path}:")
            for line in offending[:5]:
                print("   ", line[:120])
            run("git", "checkout", "--", path)
            reverted.append(path)
        else:
            print(f"ok (embed only): {path}")

    if reverted:
        # 画像はコミットさせたいので、ここでは失敗させずに警告だけ出す。
        print(f"::warning::Reverted {len(reverted)} note(s) that were edited beyond the "
              f"infographic line: {', '.join(reverted)}")
        print(f"\nReverted {len(reverted)} note(s) to HEAD; only the images were kept.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
