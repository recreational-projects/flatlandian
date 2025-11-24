"""Contains `IntVector2` class."""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Sequence

import pygame as pg

if TYPE_CHECKING:
    from collections.abc import Iterable


@dataclass(frozen=True)
class IntVector2:
    """A 2-dimensional integer vector.

    `IntVector2() -> IntVector2(0, 0)`

    `IntVector2(x: int, y: int) -> IntVector2`

    `IntVector2(int, int) -> IntVector2`

    `IntVector2((int, int)) -> IntVector2`

    Attempting to construct with `float` parameters raises `TypeError`.

    Equivalents to these `pygame.Vector2` constructors aren't yet supported:

    `Vector2(int) -> Vector2`

    `Vector2(Vector2) -> Vector2`
    """

    x: int = 0
    """x coordinate."""
    y: int = 0
    """y coordinate."""



    def __init__(self, *args: int | pg.typing.IntPoint, **kwargs: int) -> None:
        """Initialize `IntVector2` instance."""
        if args:
            if len(args) > 2:  # noqa: PLR2004
                err_msg = f"Expected 1 or 2 args, got {len(args)}"
                raise TypeError(err_msg)

            if len(args) == 1 and not isinstance(args[0], int):
                try:
                    super().__setattr__("x", args[0][0])
                    super().__setattr__("y", args[0][1])
                except TypeError as err:
                    raise TypeError from err

            if not isinstance(args[0], int) or not isinstance(args[1], int):
                err_msg = f"Expected `int`s; got ({type(args[0])}, {type(args[1])})"
                raise TypeError(err_msg)

            super().__setattr__("x", args[0])
            super().__setattr__("y", args[1])

        elif kwargs:
            super().__setattr__("x", kwargs["x"])
            super().__setattr__("y", kwargs["y"])

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
