"""Tests for `geometry` module."""

from flatlandian import geometry
from flatlandian.grid import Grid


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
