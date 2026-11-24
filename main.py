"""Entry for make.fun bounty u-0xb3e689-one-star-review-of-something-essential-c7234629.

Writes one single-line one-star review of an everyday essential to
/output/entry.txt. Standard library only; deterministic: the same line
every run.

The review: gravity, filed deadpan as a real complaint — no off switch,
drops everything you own, charges nothing for the damage — and the turn
lands in the last few words, the review-format closer "Would not
recommend." 117 characters, one line, inside the 1-160 gate.
"""

import os

LINE = (
    "One star. Gravity has no off switch, drops everything I own, "
    "and charges nothing for the damage. Would not recommend."
)


def main():
    if not 1 <= len(LINE) <= 160:
        raise ValueError("entry line must be 1-160 characters, got %d" % len(LINE))
    if "\n" in LINE:
        raise ValueError("entry must be a single line")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
