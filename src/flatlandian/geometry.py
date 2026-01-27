"""Contains general geometry functions."""

from __future__ import annotations

import itertools
from statistics import fmean
from typing import TYPE_CHECKING

from pygame import Rect
from pygame.math import Vector2

from flatlandian.int_vector2 import IntVector2

if TYPE_CHECKING:
    from collections.abc import Iterable


def mean_vector(vec2s: Iterable[Vector2]) -> Vector2:
    """Return mean vector of `vec2s`."""
    return Vector2(fmean(vec.x for vec in vec2s), fmean(vec.y for vec in vec2s))


def absolute_bearing(vec2: Vector2 | IntVector2) -> float:
    """Return 0 <= degrees < 360, from +ve y-axis in direction of +ve x-axis.

    Clockwise in a conventional system (+x right, +y up).

    Anticlockwise in Pygame / other graphics implementations (+x right, +y down).
    """
    if isinstance(vec2, IntVector2):
        vec2 = vec2.as_vector2

    return (90 - vec2.angle) % 360


def relative_bearing(bearing1: float, bearing2: float) -> float:
    """Return -180 < degrees <= 180, from +ve y-axis in direction of +ve x-axis.

    Clockwise in a conventional system (+x right, +y up).

    Anticlockwise in Pygame / other graphics implementations (+x right, +y down).
    """
    bearing = ((bearing2 - bearing1 - 180) % 360) - 180
    return 180 if bearing == -180 else bearing  # noqa: PLR2004


def cells_in_rect(rect: Rect) -> set[IntVector2]:
    """Return all cells in `rect`."""
    return {
        IntVector2(x, y)
        for x, y in itertools.product(
            range(rect.left, rect.right),
            range(rect.top, rect.bottom),
        )
    }


def cells_in_circle(*, center: IntVector2, radius: int) -> set[IntVector2]:
    """Return all cells in the circle."""
    rect = Rect(center.x - radius, center.y - radius, radius * 2, radius * 2).inflate(
        1, 1
    )
    return {
        cell
        for cell in cells_in_rect(rect)
        if (cell - center).as_vector2.length_squared() < radius**2
    }
