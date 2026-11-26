#!/usr/bin/env python3
"""The Absurd Clause Contest — entry program (program/v1, python3.13).

Writes one original English sentence — an absurd clause that could sit
buried deep inside a terms-of-service agreement — to entry.txt in the
output directory.

The clause was drafted from the design in DESIGN.md and chosen by a local
pairwise tournament of 18 candidates (see CANDIDATES.md): it opens with
textbook boilerplate ("Section 14.2", "shall be transferred") and lands on
one concrete absurd image, in a single tight sentence of 106 characters.

Deterministic: the output bytes are a fixed constant, identical on every
run. Standard library only (os).
"""

import os

ENTRY = (
    "Section 14.2: If you die while using the Service, "
    "your account shall be transferred to your nearest goose."
)


def write_entry(output_dir: str) -> str:
    """Write the clause to entry.txt in output_dir; return the path."""
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    return path


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    write_entry(output_dir)


if __name__ == "__main__":
    main()
