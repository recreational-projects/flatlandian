"""Tests for `Entity` class."""

from pygame import Vector2

from flatlandian.entity import Entity
from flatlandian.world import World


def test_create() -> None:
    """Test that `World` can be created, and initial state."""
    # arrange
    # act
    w = World(size_from_sequence=(1, 1))
    # assert
    assert w
    assert w.size == Vector2(1, 1)
    assert not w.centered_origin
    assert len(w.entities) == 0
    assert w.origin_offset == Vector2(0, 0)
    assert (
        repr(w) == "World("
        "size=Vector2(1, 1), entities=set(), centered_origin=False, step_counter=0"
        ")"
    )
    assert str(w) == "World(size=[1, 1], origin_offset=[0, 0])"


def test_create__optional_fields() -> None:
    """Test that `World` can be created, and initial state."""
    # arrange
    # act
    w = World(size_from_sequence=(1, 1), centered_origin=True)
    # assert
    assert w
    assert w.centered_origin
    assert w.origin_offset == Vector2(0.5, 0.5)
    assert (
        repr(w) == "World("
        "size=Vector2(1, 1), entities=set(), centered_origin=True, step_counter=0"
        ")"
    )
    assert str(w) == "World(size=[1, 1], origin_offset=[0.5, 0.5])"


def test_random_position() -> None:
    """TO DO."""
    # arrange
    w = World(size_from_sequence=(1, 1))
    # act
    w.random_position()


def test_random_position__centered_origin() -> None:
    """TO DO."""
    # arrange
    w = World(size_from_sequence=(1, 1), centered_origin=True)
    # act
    w.random_position()


def test_add_entity() -> None:
    """Test that an `Entity` can be added to the `World`."""
    # arrange
    w = World(size_from_sequence=(100, 100))
    e = Entity(position=Vector2(), velocity=Vector2())
    # act
    w.add_entity(e)
    # assert
    assert w.entities == {e}


def test_position_in_bounds() -> None:
    """Test that position is in bounds."""
    # arrange
    w = World(size_from_sequence=(2, 2))
    points = [Vector2(_) for _ in [(0, 0), (0, 2), (2, 2), (2, 0)]]
    # act
    result = [w.position_is_in_bounds(p) for p in points]
    # assert
    assert False not in result


def test_position_in_bounds__centered_origin() -> None:
    """Test that position is in bounds."""
    # arrange
    w = World(size_from_sequence=(2, 2), centered_origin=True)
    points = [Vector2(_) for _ in [(-1, -1), (-1, 1), (1, -1), (0.5, 0.5)]]
    # act
    result = [w.position_is_in_bounds(p) for p in points]
    # assert
    assert False not in result


def test_position_in_bounds__negative() -> None:
    """Test that position is not in bounds."""
    # arrange
    w = World(size_from_sequence=(2, 2), centered_origin=True)
    points = [Vector2(_) for _ in [(0, -2), (2, 0), (0, 2), (-2, 0)]]
    # act
    result = [not w.position_is_in_bounds(p) for p in points]
    # assert
    assert False not in result


def test_position_in_bounds__centered_origin__negative() -> None:
    """Test that position is not in bounds."""
    w = World(size_from_sequence=(2, 2))
    points = [Vector2(_) for _ in [(1, -1), (3, 1), (1, 3), (-1, 1)]]
    # act
    result = [not w.position_is_in_bounds(p) for p in points]
    # assert
    assert False not in result
