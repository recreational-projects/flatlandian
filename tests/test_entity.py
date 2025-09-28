"""Tests for `Entity` class."""

from pygame import Vector2

from flatlandian.entity import Entity


def test_create() -> None:
    """Test `Entity` can be created, and initial state."""
    # arrange
    # act
    e = Entity(position=Vector2(), velocity=Vector2())
    # assert
    assert e.position == Vector2(0, 0)
    assert e.velocity == Vector2(0, 0)
    assert e.acceleration is None
    assert e.radius == 0
    assert e.name is None
    assert (
        repr(e) == "Entity("
        "position=Vector2(0, 0), "
        "velocity=Vector2(0, 0), "
        "acceleration=None, "
        "radius=0, "
        "name=None"
        ")"
    )
    assert (
        str(e) == "Entity("
        "position=Vector2(0, 0), "
        "velocity=Vector2(0, 0), "
        "acceleration=None, "
        "radius=0, "
        "name=None"
        ")"
    )


def test_create_optional_fields() -> None:
    """Test `Entity` can be created, and initial state differs from default."""
    # arrange
    # act
    e = Entity(
        position=Vector2(),
        velocity=Vector2(),
        acceleration=Vector2(1, 1),
        radius=1,
        name="test",
    )
    # assert
    assert e.acceleration == Vector2(1, 1)
    assert e.radius == 1
    assert e.name == "test"
    assert (
        repr(e) == "Entity("
        "position=Vector2(0, 0), "
        "velocity=Vector2(0, 0), "
        "acceleration=Vector2(1, 1), "
        "radius=1, "
        "name='test')"
    )
    assert (
        str(e) == "Entity("
        "position=Vector2(0, 0), "
        "velocity=Vector2(0, 0), "
        "acceleration=Vector2(1, 1), "
        "radius=1, "
        "name='test')"
    )


def test_move() -> None:
    """Test `Entity` linear move."""
    # arrange
    e = Entity(position=Vector2(), velocity=Vector2(1, 1))
    # act
    e.move(delta_time=1)
    # assert
    assert e.position == Vector2(1, 1)
