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


def test_create_from_3_ints_raises_error() -> None:
    """Test `IntVector2` can't be created from 3 `ints`."""
    # arrange
    # act, assert
    with pytest.raises(TypeError):
        IntVector2(3, 4, 5)  # type: ignore[call-arg]


def test_create_from_float_raises_error() -> None:
    """Test `IntVector2` can't be created with a `float`."""
    # arrange
    # act, assert
    with pytest.raises(TypeError):
        IntVector2(3.4, 5)  # type: ignore[arg-type]


def test_create_zero_args() -> None:
    """Test zero vector can be created from zero arguments."""
    # arrange
    # act
    v = IntVector2()
    # assert
    assert v.x == 0
    assert v.y == 0


def test_create_from_kwargs() -> None:
    """Test `IntVector2` can be created from `x` and `y` keyword `int`s."""
    # arrange
    # act
    v = IntVector2(x=1, y=2)
    # assert
    assert v.x == 1
    assert v.y == 2


def test_from_point() -> None:
    """Test `IntVector2` can be created from 2-sequence of `int`s."""
    # arrange
    # act
    v0 = IntVector2.from_point((1, 2))
    v1 = IntVector2.from_point([1, 2])

    # assert
    assert v0.x == v1.x == 1
    assert v1.y == v1.y == 2


def test_from_point_3_tuple_raises_error() -> None:
    """Test `IntVector2` can't be created from 3-tuple `ints`."""
    # arrange
    # act
    with pytest.raises(TypeError):
        IntVector2.from_point((1, 2, 3))


def test_repr() -> None:
    # arrange
    # act
    v = IntVector2(x=1, y=2)
    # assert
    assert repr(v) == "IntVector2(1, 2)"


def test_str() -> None:
    # arrange
    # act
    v = IntVector2(x=1, y=2)
    # assert
    assert str(v) == "[1, 2]"


def test_xy() -> None:
    """Test `.xy` property."""
    # arrange
    # act
    v = IntVector2(x=1, y=2)
    # assert
    assert v.xy == (1, 2)


def test_get_item() -> None:
    """Test that values can be accessed by index."""
    # arrange
    # act
    v = IntVector2(9, 10)
    # assert
    assert v[0] == 9
    assert v[1] == 10


def test_add_int_vector2() -> None:
    """Test adding another `IntVector2`."""
    # arrange
    # act
    v = IntVector2(1, 2) + IntVector2(3, 4)
    # assert
    assert v.x == 4
    assert v.y == 6


def test_add_2_sequence() -> None:
    """Test adding a pair of `int`s."""
    # arrange
    # act
    v = IntVector2(1, 2) + (3, 4)  # noqa: RUF005
    # assert
    assert v.x == 4
    assert v.y == 6


def test_add_3_tuple_raises_error() -> None:
    """Test adding a 3-sequence."""
    # arrange
    # act, assert
    with pytest.raises(TypeError):
        IntVector2(1, 2) + (3, 4, 5)  # noqa: RUF005


def test_radd_2_tuple() -> None:
    """Test adding a 2-tuple."""
    # arrange
    # act
    v = (7, 8) + IntVector2(5, 6)  # noqa: RUF005
    # assert
    assert v.x == 12
    assert v.y == 14


def test_sub_int_vector2() -> None:
    """Test subtracting another `IntVector2`."""
    # arrange
    # act
    v = IntVector2(1, 2) - IntVector2(3, 5)
    # assert
    assert v.x == -2
    assert v.y == -3


def test_sub_2_tuple() -> None:
    """Test subtracting a 2-tuple."""
    # arrange
    # act
    v = IntVector2(1, 2) - (3, 5)
    # assert
    assert v.x == -2
    assert v.y == -3


def test_sub_3_tuple_raises_error() -> None:
    """Test subtracting a 3-sequence."""
    # arrange
    # act, assert
    with pytest.raises(TypeError):
        IntVector2(1, 2) - (3, 4, 5)


def test_rsub_2_tuple() -> None:
    """Test subtracting from a 2-tuple."""
    # arrange
    # act
    v = (3, 5) - IntVector2(1, 2)
    # assert
    assert v.x == 2
    assert v.y == 3


def test_mul() -> None:
    """Test multiplying by int."""
    # arrange
    # act
    v = IntVector2(7, 8) * 4
    # assert
    assert v.x == 28
    assert v.y == 32


def test_rmul() -> None:
    """Test multiplying int."""
    # arrange
    # act
    v = 5 * IntVector2(7, 8)
    # assert
    assert v.x == 35
    assert v.y == 40
