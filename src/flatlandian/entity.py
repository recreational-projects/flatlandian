"""Contains `Entity` class."""

from __future__ import annotations

from dataclasses import dataclass

from pygame import Vector2


@dataclass(eq=False, kw_only=True)
class Entity:
    """Generic circular entity. Hashable."""

    position: Vector2
    velocity: Vector2

    acceleration: Vector2 | None = None
    radius: float = 10
    name: str | None = None

    @property
    def heading(self) -> float:
        """Return conventional heading from velocity.

        +ve degrees clockwise from y-axis.
        """
        return (self.velocity.angle + 90) % 360

    @property
    def speed(self) -> float:
        """Return speed from velocity."""
        return self.velocity.magnitude()

    def distance_to_squared(self: Entity, other: Entity) -> float:
        """Return square of distance between self and other."""
        return (other.position - self.position).magnitude_squared()

    def stop(self) -> None:
        """Stop the entity."""
        if self.acceleration:
            self.acceleration = Vector2(0, 0)

        self.velocity = Vector2(0, 0)

    def move(self, delta_time: float) -> None:
        """Move the entity over `delta time`."""
        if self.acceleration:
            self.velocity += self.acceleration * delta_time

        self.position += self.velocity * delta_time

    def update(self, delta_time: float) -> None:
        """Update the entity."""
        self.move(delta_time)
