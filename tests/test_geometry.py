"""Tests for `geometry` module."""

from pygame.math import Vector2

from flatlandian import geometry
from flatlandian.grid import Grid


def test_mean_vector() -> None:
    """Test that mean vector can be derived."""
    # arrange
    vecs = [Vector2(1, 1), Vector2(-2, 2), Vector2(2, 3), Vector2(2, 0)]
    # act
    mean = geometry.mean_vector(vecs)
    # assert
    assert mean == Vector2(0.75, 1.5)


def test_absolute_bearing__vector2() -> None:
    """Test that bearing can be derived from `Vector2`."""
    # arrange
    vecs = [v.as_vector2 for v in Grid.DIRECTIONS]
    # act
    bearings = [geometry.absolute_bearing(v) for v in vecs]
    # assert
    assert bearings == [0, 45, 90, 135, 180, 225, 270, 315]


def test_absolute_bearing__int_vector2() -> None:
    """Test that bearing can be derived from `IntVector2`."""
    # arrange
    # act
    bearings = [geometry.absolute_bearing(v) for v in Grid.DIRECTIONS]
    # assert
    assert bearings == [0, 45, 90, 135, 180, 225, 270, 315]


def test_relative_bearing() -> None:
    """Test that bearing can be derived from two bearings."""
    # arrange
    bearings = [geometry.absolute_bearing(v) for v in Grid.DIRECTIONS]
    # act
    bearings_from_0 = [geometry.relative_bearing(0, b) for b in bearings]
    bearings_from_180 = [geometry.relative_bearing(180, b) for b in bearings]
    # assert
    assert bearings_from_0 == [0, 45, 90, 135, 180, -135, -90, -45]
    assert bearings_from_180 == [180, -135, -90, -45, 0, 45, 90, 135]
