import os
import random
from typing import List


def clear_screen() -> None:
    os.system("cls" if os.name == "nt" else "clear")


def random_food(width: int, height: int, snake_body: List[List[int]]) -> List[int]:
    while True:
        x = random.randint(0, width - 1)
        y = random.randint(0, height - 1)
        if [x, y] not in snake_body:
            return [x, y]


def load_high_score(path: str) -> int:
    try:
        with open(path, "r", encoding="utf-8") as f:
            return int(f.read().strip() or "0")
    except FileNotFoundError:
        return 0
    except ValueError:
        return 0


def save_high_score(path: str, score: int) -> None:
    with open(path, "w", encoding="utf-8") as f:
        f.write(str(score))
