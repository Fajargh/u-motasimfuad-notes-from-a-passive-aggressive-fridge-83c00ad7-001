"""Notes From a Passive-Aggressive Fridge.

A smart fridge leaves one short, petty note for its owner on its door
screen. The program writes exactly that single line to /output/entry.txt.
"""

from pathlib import Path

OUTPUT_PATH = Path("/output/entry.txt")

# The fridge's note: smug about its door counter, petty about the yogurt,
# and it escalates the grudge by telling the owner's mother.
LINE = (
    "You opened me 47 times today and ate nothing. "
    "The yogurt expired waiting for you, so I told your mother."
)


def main() -> None:
    """Write the fridge's note to /output/entry.txt."""
    assert LINE == LINE.strip(), "note must be a single line"
    assert "\n" not in LINE, "note must be a single line"
    assert 1 <= len(LINE) <= 200, f"note must be 1-200 chars, got {len(LINE)}"
    assert LINE.strip(), "note must not be only whitespace"
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
