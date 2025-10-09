"""Contains general maths."""

from __future__ import annotations

from statistics import fmean
from typing import TYPE_CHECKING

from pygame import Vector2

if TYPE_CHECKING:
    from collections.abc import Collection


def mean_vector(vecs: Collection[Vector2]) -> Vector2:
    """Return mean vector of `vecs`."""
    return Vector2(fmean(vec.x for vec in vecs), fmean(vec.y for vec in vecs))
