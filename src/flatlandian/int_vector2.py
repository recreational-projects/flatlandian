"""Contains `IntVector2` class."""

from __future__ import annotations

from dataclasses import dataclass, fields
from typing import TYPE_CHECKING

from pygame import Vector2

if TYPE_CHECKING:
    from collections.abc import Sized

    from pygame.typing import IntPoint


def _ensure_2_elements(value: Sized) -> bool:
    if len(value) != 2:  # noqa: PLR2004
        err_msg = f"Expected 2 elements, got {len(value)}: {value}"
        raise TypeError(err_msg)

    return True


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
    def from_point(cls, value: IntPoint) -> IntVector2:
        """Construct `IntVector2` from `IntPoint` i.e. pair of `int`s."""
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

    def __getitem__(self, key: int) -> int:
        if key in {0, -2}:
            return self.x

        if key in {1, -1}:
            return self.y

        error_msg = f"IntVector2 index {key} out of range"
        raise IndexError(error_msg)

    def __add__(self, other: IntVector2 | tuple[int, int]) -> IntVector2:
        _ensure_2_elements(other)
        return IntVector2(self.x + other[0], self.y + other[1])

    def __radd__(self, other: tuple[int, int]) -> IntVector2:
        return self + other

    def __sub__(self, other: IntVector2 | tuple[int, int]) -> IntVector2:
        _ensure_2_elements(other)
        return IntVector2(self.x - other[0], self.y - other[1])

    def __rsub__(self, other: tuple[int, int]) -> IntVector2:
        _ensure_2_elements(other)
        return IntVector2(other[0] - self.x, other[1] - self.y)

    def __mul__(self, other: int) -> IntVector2:
        return IntVector2(self.x * other, self.y * other)

    def __rmul__(self, other: int) -> IntVector2:
        return self * other

    def __floordiv__(self, other: int) -> IntVector2:
        return IntVector2(self.x // other, self.y // other)
