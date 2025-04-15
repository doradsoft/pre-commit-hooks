from __future__ import annotations

import argparse
from collections.abc import Sequence
from typing import Any

import json5


def raise_duplicate_keys(ordered_pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    d = {}
    for key, val in ordered_pairs:
        if key in d:
            raise ValueError(f'Duplicate key: {key}')
        else:
            d[key] = val
    return d


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='Filenames to check.')
    args = parser.parse_args(argv)

    retval = 0
    for filename in args.filenames:
        with open(filename, 'r', encoding='UTF-8') as f:
            try:
                json5.load(f, object_pairs_hook=raise_duplicate_keys)
            except ValueError as exc:
                print(f'{filename}: Failed to json5 decode ({exc})')
                retval = 1
    return retval


if __name__ == '__main__':
    raise SystemExit(main())
