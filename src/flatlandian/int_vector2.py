"""Contains `IntVector2` class."""

from __future__ import annotations

from dataclasses import dataclass, fields
from typing import TYPE_CHECKING

from pygame import Vector2

if TYPE_CHECKING:
    from collections.abc import Sized


def _ensure_2_elements(value: Sized) -> bool:
    if len(value) != 2:  # noqa: PLR2004
        err_msg = f"Expected 2 elements, got {len(value)} elements."
        raise TypeError(err_msg)

    return True


@dataclass
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

    _x: int
    """x coordinate."""
    _y: int
    """y coordinate."""

    def __init__(self, x: int=0, y: int=0) -> None:
        """Initialize a vector from `x` and `y`."""
        if not isinstance(x, int) or not isinstance(y, int):
            err_msg = f"Expected 2 `int`s; got {x=}, {y=}"  # type: ignore[unreachable]
            raise TypeError(err_msg)

        self._x = x
        self._y = y

    @property
    def x(self) -> int:
        """Return `x` coordinate."""
        return self._x

    @property
    def y(self) -> int:
        """Return `y` coordinate."""
        return self._y

    @classmethod
    def from_tuple(cls, value: tuple[int, int]) -> IntVector2:
        """Construct vector from `tuple` of `int`s.

        For compatibility with Pygame functions.
        """
        _ensure_2_elements(value)
        return cls(value[0], value[1])

    @property
    def as_vector2(self) -> Vector2:
        """Return `pygame.Vector2`, i.e. float coordinates.

        For compatibility with Pygame functions.
        """
        return Vector2(self.x, self.y)

    def __len__(self) -> int:
        return len(fields(self))

    def __add__(self, other: IntVector2 | tuple[int, int]) -> IntVector2:
        _ensure_2_elements(other)
        if isinstance(other, IntVector2):
            return IntVector2(self.x + other.x, self.y + other.y)

        return IntVector2(self.x + other[0], self.y + other[1])

    def __radd__(self, other: tuple[int, int]) -> IntVector2:
        _ensure_2_elements(other)
        return IntVector2(other[0] + self.x, other[1] + self.y)

    def __sub__(self, other: IntVector2 | tuple[int, int]) -> IntVector2:
        _ensure_2_elements(other)
        if isinstance(other, IntVector2):
            return IntVector2(self.x - other.x, self.y - other.y)

        return IntVector2(self.x - other[0], self.y - other[1])

    def __rsub__(self, other: tuple[int, int]) -> IntVector2:
        _ensure_2_elements(other)
        return IntVector2(other[0] - self.x, other[1] - self.y)

    def __mul__(self, other: int) -> IntVector2:
        return IntVector2(other * self.x, other * self.y)

    def __floordiv__(self, other: int) -> IntVector2:
        return IntVector2(self.x // other, self.y // other)
