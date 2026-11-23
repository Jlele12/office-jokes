#!/usr/bin/env python3
"""Office-jokes entry for make.fun's "Make the AI Judge Laugh: Office Jokes".

Writes exactly one joke (under 200 characters) to /output/entry.txt.
"""
import os

JOKE = (
    "HR approved an AI assistant for morale. Every Monday it sends Dave "
    "from accounting the same sympathy GIF. HR says engagement is way up."
)


def main() -> int:
    assert len(JOKE) < 200, "joke must stay under 200 chars"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")
    print(JOKE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
