"""Contains general geometry functions."""

from __future__ import annotations

from statistics import fmean
from typing import TYPE_CHECKING

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
