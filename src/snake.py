from dataclasses import dataclass
from typing import List, Tuple

Direction = Tuple[int, int]
Point = List[int]  # [x, y]


@dataclass
class Snake:
    body: List[Point]          # cabeza es body[0]
    direction: Direction       # (dx, dy)

    def head(self) -> Point:
        return self.body[0]

    def set_direction(self, new_dir: Direction) -> None:
        """Evita girar 180° cuando la serpiente tiene más de 1 segmento."""
        dx, dy = self.direction
        ndx, ndy = new_dir

        if len(self.body) > 1 and (dx + ndx, dy + ndy) == (0, 0):
            return
        self.direction = new_dir

    def next_head(self) -> Point:
        dx, dy = self.direction
        hx, hy = self.head()
        return [hx + dx, hy + dy]

    def move(self, grow: bool) -> None:
        """Inserta nueva cabeza; si no crece, quita la cola."""
        self.body.insert(0, self.next_head())
        if not grow:
            self.body.pop()
