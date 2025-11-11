"""Contains `IntVector2` class."""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

import pygame as pg

if TYPE_CHECKING:
    from pygame.typing import IntPoint


@dataclass(frozen=True)
class IntVector2:
    """Integer point."""

    x: int = 0
    """x coordinate."""
    y: int = 0
    """y coordinate."""

    def __post_init__(self) -> None:
        if not isinstance(self.x, int) or not isinstance(self.y, int):
            err_msg = f"Expected 2 `int`s; got x={self.x}, y={self.y}"  # type: ignore[unreachable]
            raise TypeError(err_msg)

    @classmethod
    def from_tuple(cls, value: tuple[int, int]) -> IntVector2:
        """For compatibility with Pygame functions."""
        return cls(value[0], value[1])

    @property
    def as_vector2(self) -> pg.Vector2:
        """For compatibility with Pygame functions."""
        return pg.Vector2(self.x, self.y)

    def __add__(self, other: IntVector2 | IntPoint) -> IntVector2:
        if isinstance(other, IntVector2):
            return IntVector2(self.x + other.x, self.y + other.y)

        return IntVector2(self.x + other[0], self.y + other[0])

    def __sub__(self, other: IntVector2 | IntPoint) -> IntVector2:
        if isinstance(other, IntVector2):
            return IntVector2(self.x - other.x, self.y - other.y)

        return IntVector2(self.x - other[0], self.y - other[0])

    def __mul__(self, other: int) -> IntVector2:
        return IntVector2(other * self.x, other * self.y)

    def __floordiv__(self, other: int) -> IntVector2:
        return IntVector2(self.x // other, self.y // other)
