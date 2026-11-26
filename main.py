#!/usr/bin/env python3
"""One Line to Your Younger Self — writes the entry to /output/entry.txt."""
import os

LINE = (
    "The people you are killing yourself to impress will forget your name — "
    "the ones who remember it are the ones you keep walking past."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/tmp/smoke-younger-1")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(f"wrote {len(LINE)} chars to {out_dir}/entry.txt")


if __name__ == "__main__":
    main()
