"""Write the toaster error message entry to /output/entry.txt.

One line, 76 characters (limit 120) -- no trailing newline."""

from pathlib import Path

ENTRY = "ERROR 404: BREAD NOT FOUND. Please insert bread, or lower your expectations."

def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")

if __name__ == "__main__":
    main()
