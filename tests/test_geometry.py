"""Tests for `geometry` module."""

from pygame import Vector2

from flatlandian import geometry
from flatlandian.int_vector2 import IntVector2


def test_absolute_bearing__vector2() -> None:
    """Test that bearing can be derived from `Vector2`."""
    # arrange
    dirs = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
    vecs = [Vector2(c) for c in dirs]
    # act
    angles = [geometry.absolute_bearing(v) for v in vecs]
    # assert
    assert angles == [0, 45, 90, 135, 180, 225, 270, 315]


def test_absolute_bearing__intvector2() -> None:
    """Test that bearing can be derived from `IntVector2`."""
    # arrange
    dirs = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
    vecs = [IntVector2(c) for c in dirs]
    # act
    angles = [geometry.absolute_bearing(v) for v in vecs]
    # assert
    assert angles == [0, 45, 90, 135, 180, 225, 270, 315]
