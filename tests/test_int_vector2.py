"""Tests for `IntVector2` class."""

import pytest

from flatlandian.int_vector2 import IntVector2


def test_create_from_2_ints() -> None:
    """Test `IntVector2` can be created from 2 `ints`."""
    # arrange
    # act
    v = IntVector2(1, 2)
    # assert
    assert v.x == 1
    assert v.y == 2


def test_create_from_float_raises_error() -> None:
    """Test `IntVector2` can't be created with a `float`."""
    # arrange
    # act
    with pytest.raises(TypeError):
        IntVector2(3.4, 5)  # type: ignore[arg-type]


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


def test_add_int_vector2() -> None:
    """Test adding another `IntVector2`."""
    # arrange
    v0 = IntVector2(1, 2)
    # act
    v = v0 + IntVector2(3, 4)
    # assert
    assert v.x == 4
    assert v.y == 6


def test_add_2_tuple() -> None:
    """Test adding a 2-tuple."""
    # arrange
    v0 = IntVector2(1, 2)
    t = (3, 4)
    # act
    v = v0 + t
    # assert
    assert v.x == 4
    assert v.y == 6


def test_sub_int_vector2() -> None:
    """Test subtracting another `IntVector2`."""
    # arrange
    v0 = IntVector2(1, 2)
    # act
    v = v0 - IntVector2(3, 5)
    # assert
    assert v.x == -2
    assert v.y == -3


def test_sub_2_tuple() -> None:
    """Test subtracting a 2-tuple."""
    # arrange
    v0 = IntVector2(1, 2)
    t = (3, 5)
    # act
    v = v0 - t
    # assert
    assert v.x == -2
    assert v.y == -3
