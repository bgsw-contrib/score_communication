#!/usr/bin/env python3
"""Normalize/verify that files end with exactly one trailing newline."""

import sys


def normalize(data: bytes) -> bytes:
    if not data:
        return data
    return data.rstrip(b"\n") + b"\n"


def main(argv: list[str]) -> int:
    check = "--check" in argv
    files = [a for a in argv[1:] if a != "--check"]

    violations = []
    for path in files:
        with open(path, "rb") as f:
            data = f.read()
        fixed = normalize(data)
        if fixed == data:
            continue
        if check:
            violations.append(path)
        else:
            with open(path, "wb") as f:
                f.write(fixed)

    if check and violations:
        sys.stderr.write("The following files must end with exactly one newline:\n")
        for path in violations:
            sys.stderr.write(f"  {path}\n")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
