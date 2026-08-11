"""PostToolUse hook: warn when an edited decklist no longer totals exactly 100 cards.

Reads the hook JSON from stdin, inspects the edited file if it's a .txt decklist
(lines matching "<qty> <card name>"), and exits 2 with a stderr message when the
total differs from 100 so Claude sees the warning immediately.
"""
import json
import os
import re
import sys


def main() -> int:
    try:
        data = json.load(sys.stdin)
    except Exception:
        return 0

    tool_input = data.get("tool_input") or {}
    file_path = tool_input.get("file_path", "")
    if not file_path.lower().endswith(".txt"):
        return 0

    total = 0
    deck_lines = 0
    try:
        with open(file_path, encoding="utf-8") as f:
            for line in f:
                m = re.match(r"\s*(\d+)\s+\S", line)
                if m:
                    total += int(m.group(1))
                    deck_lines += 1
    except OSError:
        return 0

    # Not a decklist (no "<qty> <name>" lines) — stay silent.
    if deck_lines < 10:
        return 0

    if total != 100:
        diff = total - 100
        sys.stderr.write(
            f"DECK COUNT WARNING: {os.path.basename(file_path)} totals {total} cards "
            f"({'+' if diff > 0 else ''}{diff} vs the required 100 including commander). "
            "Fix the count before finishing."
        )
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
