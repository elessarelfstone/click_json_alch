import json
from pathlib import Path
from collections import deque


def countries_gen(file: str, size: int = 500):
    countries = json.loads(Path(file).read_text())
    cnt = 0
    c_deque = deque(countries)
    while cnt <= size:

        for c in c_deque:
            yield c
            cnt += 1

        c_deque = deque(countries)
