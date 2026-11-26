"""Write the entry line to the output directory.

Competition: "One Line, One Chill" on make.fun — one line of horror,
a single sentence of under 200 characters that has to frighten a
reader in one breath. No setup, no paragraph, no second chance. The
harness runs `python3 main.py` and reads
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`).
"""

import os

LINE = "The baby monitor whispered my name tonight — in my voice, from the nursery, while I was holding the baby downstairs."

OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> None:
    # Self-check: one non-blank line, strictly under 200 characters.
    assert LINE.strip(), "entry line must not be blank"
    assert "\n" not in LINE.strip(), "entry line must be a single line"
    assert 1 <= len(LINE) < 200, "entry line must be under 200 characters"
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(os.path.join(OUT_DIR, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
