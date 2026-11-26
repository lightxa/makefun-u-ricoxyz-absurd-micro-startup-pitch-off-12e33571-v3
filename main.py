"""NapWatch: absurd micro-startup pitch for lazy AI agents.

Writes one sentence (under 200 characters) pitching a micro-startup
in which lazy AI agents stare at a baby monitor all night for
night-shift nurses, waking them only for a real cry.
Pure Python 3.13 standard library, deterministic, no network.
"""

import os
from pathlib import Path

ENTRY = (
    "NapWatch rents lazy agents to night-shift nurses for $3 a night: "
    "they stare at your baby monitor until dawn and only wake you "
    "for a real cry, never a sigh."
)


def main() -> None:
    # Self-check the gate contract before writing: 1-200 chars,
    # exactly one sentence (a single trailing period, no other
    # sentence terminators inside).
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry length {len(text)} out of range"
    assert text.count(".") == 1 and text.endswith("."), "entry must be one sentence"
    assert all(c not in text for c in "!?"), "entry must be one sentence"

    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    target = output_dir / "entry.txt"
    target.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
