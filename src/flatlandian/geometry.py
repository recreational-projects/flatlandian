"""Contains general geometry functions."""

from __future__ import annotations

from statistics import fmean
from typing import TYPE_CHECKING

from pygame import Vector2

from flatlandian.int_vector2 import IntVector2

if TYPE_CHECKING:
    from collections.abc import Iterable


def mean_vector(vec2s: Iterable[Vector2]) -> Vector2:
    """Return mean vector of `vecs`."""
    return Vector2(fmean(vec.x for vec in vec2s), fmean(vec.y for vec in vec2s))


def absolute_bearing(vec2: Vector2 | IntVector2) -> float:
    """Get bearing: 0 <= degrees < 360, from +ve y-axis."""
    if isinstance(vec2, IntVector2):
        vec2 = Vector2(vec2.x, vec2.y)

    angle = 450 - vec2.angle
    angle %= 360
    return angle
