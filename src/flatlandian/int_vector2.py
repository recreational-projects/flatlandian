"""Contains `IntVector2` class."""

from __future__ import annotations

from typing import TYPE_CHECKING

from attrs import define, field, fields, validators
from pygame.math import Vector2

if TYPE_CHECKING:
    from collections.abc import Sized

    from pygame.typing import IntPoint


def _ensure_2_elements(value: Sized) -> bool:
    """Used in arithmetic operations, not constructors."""
    if len(value) != 2:  # noqa: PLR2004
        err_msg = f"Expected 2 elements, got {len(value)}: {value}"
        raise TypeError(err_msg)

    return True


@define(frozen=True)
class IntVector2:
    """A 2-dimensional integer vector.

    Frozen and hashable (unlike pygame.Vector2).
    Supports `len` (always 2) and indexing.
    Conforms to `pygame.typing.IntPoint`.

    Constructors
    ------------
    ```
    IntVector2() -> IntVector2(0, 0)
    IntVector2(int, int) -> IntVector2
    IntVector2(x: int, y: int) -> IntVector2
    ```

    Attempting to construct with non-`int` values raises `TypeError`.

    Equivalents to these `pygame.math.Vector2` constructors aren't yet supported:
    ```
    Vector2(int) -> Vector2
    Vector2(Vector2) -> Vector2
    Vector2((x, y)) -> Vector2
    ```
    Arithmetic
    ----------
    Supports element-wise addition and subtraction of another `IntVector2`
    or `pygame.typing.IntPoint` i.e. a sequence-like of 2 `int`s.
    Returns `IntVector2`.

    Supports scalar multiplication and floor division by `int`.
    Returns `IntVector2`.
    """

    x: int = field(default=0, validator=validators.instance_of(int))
    """x coordinate. Also available via index 0 or -1."""

    y: int = field(default=0, validator=validators.instance_of(int))
    """y coordinate. Also available via index 1 or -2."""

    @classmethod
    def from_point(cls, value: IntPoint) -> IntVector2:
        """Construct `IntVector2` from a sequence of two `int`s.

        TODO: Re-implement in IntVector2().`
        """
        _ensure_2_elements(value)
        return cls(value[0], value[1])

    @property
    def as_vector2(self) -> Vector2:
        """Return `pygame.math.Vector2`, i.e. float coordinates.

        For compatibility with Pygame functions.
        """
        return Vector2(self.x, self.y)

    @property
    def xy(self) -> tuple[int, int]:
        """Return tuple."""
        return self.x, self.y

    def __repr__(self) -> str:
        return self.__class__.__name__ + f"({self.x}, {self.y})"

    def __str__(self) -> str:
        return f"[{self.x}, {self.y}]"

    def __len__(self) -> int:
        return len(fields(self))

    def __getitem__(self, key: int) -> int:
        if key in {0, -2}:
            return self.x

        if key in {1, -1}:
            return self.y

        error_msg = f"IntVector2 index {key} out of range"
        raise IndexError(error_msg)

    def __add__(self, other: IntPoint) -> IntVector2:
        _ensure_2_elements(other)
        return IntVector2(self.x + other[0], self.y + other[1])

    def __radd__(self, other: IntPoint) -> IntVector2:
        return self + other

    def __sub__(self, other: IntPoint) -> IntVector2:
        _ensure_2_elements(other)
        return IntVector2(self.x - other[0], self.y - other[1])

    def __rsub__(self, other: IntPoint) -> IntVector2:
        _ensure_2_elements(other)
        return IntVector2(other[0] - self.x, other[1] - self.y)

    def __mul__(self, other: int) -> IntVector2:
        return IntVector2(self.x * other, self.y * other)

    def __rmul__(self, other: int) -> IntVector2:
        return self * other

    def __floordiv__(self, other: int) -> IntVector2:
        return IntVector2(self.x // other, self.y // other)
