"""Contains `IntVector2` class."""

from __future__ import annotations

from dataclasses import dataclass

import pygame as pg


@dataclass(frozen=True)
class IntVector2:
    """A 2-dimensional integer vector.

    `IntVector2() -> IntVector2(0, 0)`

    `IntVector2(x: int, y: int) -> IntVector2`

    `IntVector2(int, int) -> IntVector2`

    Attempting to construct with `float` parameters raises `TypeError`.

    Equivalents to these `pygame.Vector2` constructors aren't yet supported:

    `Vector2(int) -> Vector2`

    `Vector2(Vector2) -> Vector2`

    `Vector2((x, y)) -> Vector2`
    """

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
        """Construct vector from `tuple` of `int`s.

        For compatibility with Pygame functions.
        """
        return cls(value[0], value[1])

    @property
    def as_vector2(self) -> pg.Vector2:
        """Return `pygame.Vector2`, i.e. float coordinates.

        For compatibility with Pygame functions.
        """
        return pg.Vector2(self.x, self.y)

    def __add__(self, other: IntVector2 | tuple[int, int]) -> IntVector2:
        if isinstance(other, IntVector2):
            return IntVector2(self.x + other.x, self.y + other.y)

        return IntVector2(self.x + other[0], self.y + other[1])

    def __sub__(self, other: IntVector2 | tuple[int, int]) -> IntVector2:
        if isinstance(other, IntVector2):
            return IntVector2(self.x - other.x, self.y - other.y)

        return IntVector2(self.x - other[0], self.y - other[1])

    def __mul__(self, other: int) -> IntVector2:
        return IntVector2(other * self.x, other * self.y)

    def __floordiv__(self, other: int) -> IntVector2:
        return IntVector2(self.x // other, self.y // other)
