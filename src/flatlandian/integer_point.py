"""Contains `IntegerPoint` class."""

from __future__ import annotations

from dataclasses import dataclass

import pygame as pg


@dataclass(frozen=True)
class IntegerPoint:
    """Integer point."""

    x: int
    """x coordinate."""
    y: int
    """y coordinate."""

    @classmethod
    def from_tuple(cls, value: tuple[int, int]) -> IntegerPoint:
        """For compatibility with Pygame functions."""
        return cls(value[0], value[1])

    @property
    def as_vector(self) -> pg.Vector2:
        """For compatibility with Pygame functions."""
        return pg.Vector2(self.x, self.y)

    def __add__(self, other: IntegerPoint) -> IntegerPoint:
        return IntegerPoint(self.x + other.x, self.y + other.y)

    def __sub__(self, other: IntegerPoint) -> IntegerPoint:
        return IntegerPoint(self.x - other.x, self.y - other.y)

    def __mul__(self, other: int) -> IntegerPoint:
        return IntegerPoint(other * self.x, other * self.y)

    def __floordiv__(self, other: int) -> IntegerPoint:
        return IntegerPoint(self.x // other, self.y // other)
