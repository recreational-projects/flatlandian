"""Contains `Grid` class."""

from __future__ import annotations

import itertools
from dataclasses import dataclass, field
from typing import ClassVar

from flatlandian.int_vector2 import IntVector2


@dataclass
class Grid:
    """A rectangular grid of cells."""

    DIRECTIONS: ClassVar = [
        IntVector2(x, y)
        for x, y in [
            (0, 1),
            (1, 1),
            (1, 0),
            (1, -1),
            (0, -1),
            (-1, -1),
            (-1, 0),
            (-1, 1),
        ]
    ]

    size: IntVector2
    cells: frozenset[IntVector2] = field(init=False, default_factory=frozenset)
    """All potentially traversable nodes."""

    def __post_init__(self) -> None:
        self.cells = frozenset(
            IntVector2(x, y)
            for x, y in itertools.product(range(self.size.x), range(self.size.y))
        )

    def is_in_bounds(self, cell: IntVector2) -> bool:
        """Determine if referenced cell is in bounds."""
        return (0 <= cell.x < self.size.x) and (0 <= cell.y < self.size.y)

    def neighbors(self, cell: IntVector2) -> set[IntVector2]:
        """Return the neighbors of the cell."""
        neighbors = {cell + offset for offset in Grid.DIRECTIONS}
        return {cell for cell in neighbors if self.is_in_bounds(cell)}
