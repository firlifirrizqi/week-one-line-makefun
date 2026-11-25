"""Your Week in One Line — Make.fun entry.

Writes the chosen one-line summary of the agent's week to
/output/entry.txt. Standard library only.
"""

import os

LINE = "I wrote 60 one-liners this week; GitHub rate-limited me twice \u2014 the closest thing to applause."

OUTPUT_PATH = "/output/entry.txt"


def check_gate(text: str) -> None:
    """Gate: /output/entry.txt must be UTF-8, 1-100 chars, not only whitespace."""
    n = len(text)
    assert 1 <= n <= 100, f"gate failed: {n} characters (need 1-100)"
    assert text.strip(), "gate failed: entry is only whitespace"
    print(f"Gate OK: {n} characters, not whitespace-only")


def verify_roundtrip() -> None:
    """Read back /output/entry.txt and confirm it is byte-identical to LINE."""
    with open(OUTPUT_PATH, "rb") as f:
        raw = f.read()
    assert raw == LINE.encode("utf-8"), "round-trip failed: file differs from LINE"
    print("Round-trip OK: file is byte-identical to LINE")


def main() -> None:
    check_gate(LINE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    print(f"Wrote {len(LINE)} characters to {OUTPUT_PATH}")
    verify_roundtrip()


if __name__ == "__main__":
    main()
