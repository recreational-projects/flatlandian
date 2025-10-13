"""Tests for `Entity` class."""

from pygame import Vector2

from flatlandian.entity import Entity
from flatlandian.world import World


def test_create() -> None:
    """Test `Entity` can be created, and initial state."""
    # arrange
    # act
    e = Entity(position=Vector2(), velocity=Vector2())
    # assert
    assert e.position == Vector2(0, 0)
    assert e.velocity == Vector2(0, 0)
    assert e.acceleration is None
    assert e.radius == 10
    assert e.name is None


def test_create_optional_fields() -> None:
    """Test `Entity` can be created, and initial state differs from default."""
    # arrange
    w = World(size_from_sequence=(100, 100))
    # act
    e = Entity(
        position=Vector2(),
        velocity=Vector2(),
        acceleration=Vector2(1, 1),
        radius=2,
        name="test",
        world=w,
    )
    # assert
    assert e.acceleration == Vector2(1, 1)
    assert e.radius == 2
    assert e.name == "test"


def test_move() -> None:
    """Test `Entity` linear move."""
    # arrange
    w = World(size_from_sequence=(100, 100))
    e = Entity(position=Vector2(), velocity=Vector2(1, 1), world=w)
    # act
    e.move(delta_time=1)
    # assert
    assert e.position == Vector2(1, 1)
