from typing import NamedTuple
from functools import reduce

StringRange = NamedTuple("Location", [("start", int), ("length", int)])

def clear_ranges(source: str, ranges: list[StringRange]) -> str:
    clear_result = reduce(
        lambda acc, rng: (acc[0] + source[acc[1]:rng.start], rng.start + rng.length),
        sorted(ranges, key= lambda rng: rng.start),
        ("", 0)
    )

    return clear_result[0] + source[clear_result[1]:]