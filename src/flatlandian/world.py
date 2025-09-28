"""Contains `World` class."""

from __future__ import annotations

import random
from dataclasses import InitVar, dataclass, field
from typing import TYPE_CHECKING

from pygame import Vector2

if TYPE_CHECKING:
    from collections.abc import Sequence

    from flatlandian.entity import Entity


@dataclass(kw_only=True)
class World:
    """Rectangular."""

    size_from_sequence: InitVar[Sequence[float]]
    size: Vector2 = field(init=False)
    centered_origin: bool = False
    step_counter: int = field(default=0, init=False)
    entities: set[Entity] = field(default_factory=set)

    def __post_init__(self, size_from_sequence: Sequence[float]) -> None:
        """Initialize a `World`."""
        self.size = Vector2(size_from_sequence)

    @property
    def origin_offset(self) -> Vector2:
        """Return the origin's offset."""
        return self.size / 2 if self.centered_origin else Vector2(0, 0)

    def __str__(self) -> str:
        """Human-readable description."""
        return (
            f"{type(self).__name__}("
            f"size={self.size}, origin_offset={self.origin_offset}"
            ")"
        )

    def position_is_in_bounds(self, position: Vector2, *, offset: float = 0) -> bool:
        """Return whether `position` is within the world.

        -ve/+ve offset: offset in/out from edge.
        """
        min_ = Vector2(0, 0) - self.origin_offset - Vector2(offset, offset)
        max_ = self.size - self.origin_offset + Vector2(offset, offset)
        return min_.x <= position.x <= max_.x and min_.y <= position.y <= max_.y

    def random_position(self) -> Vector2:
        """Return a uniformly distributed random position within the world."""
        return Vector2(
            random.uniform(0, self.size.x + self.origin_offset.x),
            random.uniform(0, self.size.y + self.origin_offset.y),
        )

    def random_edge_position(self, offset: float = 0) -> Vector2:
        """Return a random position on or offset from the edge of the world.

        Uniformly distributed.

        -ve/+ve offset: offset in/out from edge.
        """
        sx, sy = self.size + Vector2(2 * offset)
        distance = random.uniform(0, 2 * sx + 2 * sy)
        if distance < sx:
            point = Vector2(distance, 0)
        elif distance < sx + sy:
            point = Vector2(sx, distance - sx)
        elif distance < 2 * sx + sy:
            point = Vector2(distance - sx - sy, sy)
        else:
            point = Vector2(0, distance - 2 * sx - sy)

        return point + self.origin_offset - Vector2(offset)

    def add_entity(self, entity: Entity) -> None:
        """Add `entity` to the world."""
        self.entities.add(entity)

    def update(self, delta_time: float) -> None:
        """Update the world."""
        for entity in self.entities:
            entity.update(delta_time)

        self.step_counter += 1
