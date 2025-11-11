"""Tests for `IntVector2` class."""

from flatlandian.int_vector2 import IntVector2


def test_create_from_2_ints() -> None:
    """Test `IntVector2` can be created from 2 `ints`."""
    # arrange
    # act
    v = IntVector2(1, 2)
    # assert
    assert v.x == 1
    assert v.y == 2


def test_create_from_kwargs() -> None:
    """Test `IntVector2` can be created from `x` and `y` keyword `int`s."""
    # arrange
    # act
    v = IntVector2(x=1, y=2)
    # assert
    assert v.x == 1
    assert v.y == 2


def test_create_from_2_tuple() -> None:
    """Test `IntVector2` can be created from 2-tuple of `int`s."""
    # arrange
    # act
    v = IntVector2.from_tuple((1, 2))
    # assert
    assert v.x == 1
    assert v.y == 2


def test_create_zero_vector() -> None:
    """Test zero vector can be created from zero arguments."""
    # arrange
    # act
    v = IntVector2()
    # assert
    assert v.x == 0
    assert v.y == 0
