"""Contains `NavigationGrid` class and supporting code."""

from __future__ import annotations

import heapq
import math
from dataclasses import dataclass, field

from flatlandian.grid import Grid
from flatlandian.int_vector2 import IntVector2

_SQRT_2 = math.sqrt(2)


@dataclass(kw_only=True)
class _PrioritisedNode:
    """Wrapper for prioritised node.

    Avoids unintended prioritisation attempts on `node` itself.
    """

    node: IntVector2
    priority: float

    def __lt__(self, other: _PrioritisedNode) -> bool:
        """Determine priority for `heapq`."""
        return self.priority < other.priority


@dataclass(kw_only=True)
class _PriorityQueue:
    """Simple priority queue, using `heapq`. Specialised for holding nodes."""

    items: list[_PrioritisedNode] = field(init=False, default_factory=list)

    @property
    def is_empty(self) -> bool:
        """Check whether the queue is empty."""
        return not self.items

    def put(self, priority: float, node: IntVector2) -> None:
        """Add a node with priority."""
        heapq.heappush(self.items, _PrioritisedNode(priority=priority, node=node))

    def get(self) -> IntVector2:
        """Remove and return the highest priority node.

        NB this is the lowest `priority` value.
        """
        return heapq.heappop(self.items).node


@dataclass
class NavigationGrid(Grid):
    """A rectangular navigable grid."""

    nodes: frozenset[IntVector2] = field(init=False, default_factory=frozenset)
    """All potentially traversable nodes."""
    blocked_nodes: set[IntVector2] = field(init=False, default_factory=set)
    """Subset of `nodes` that cannot currently be traversed."""

    def __post_init__(self) -> None:
        super().__post_init__()
        self.nodes = self.cells

    def is_traversable(self, node: IntVector2) -> bool:
        """Return `True` if the node is traversable, else `False`."""
        return node in self.nodes and node not in self.blocked_nodes

    def _reachable_neighbors(self, node: IntVector2) -> set[IntVector2]:
        """Return `node`'s reachable (by movement) neighbors."""
        reachable_neighbors: set[IntVector2] = set()
        for dir_ in Grid.DIRECTIONS:
            neighbor = IntVector2(node.x + dir_.x, node.y + dir_.y)
            if self.is_traversable(neighbor):
                reachable_neighbors.add(neighbor)

        return reachable_neighbors

    def cost(self, from_node: IntVector2, to_node: IntVector2) -> float:
        """Calculate the cost from node to a neighbor.

        Always 1 for cardinal, sqrt(2) for diagonal.
        """
        if to_node not in self.neighbors(from_node):
            err_msg = (
                f"Can't calculate cost from {from_node} to {to_node}: not neighbors"
            )
            raise ValueError(err_msg)

        dist = abs(from_node.x - to_node.x) + abs(from_node.y - to_node.y)
        if dist == 2:  # noqa: PLR2004
            return _SQRT_2

        return 1

    def _search(
        self,
        start_node: IntVector2,
        goal_node: IntVector2,
    ) -> dict[IntVector2, IntVector2 | None]:
        came_from: dict[IntVector2, IntVector2 | None] = {start_node: None}
        cost_so_far: dict[IntVector2, float] = {start_node: 0}
        frontier: _PriorityQueue = _PriorityQueue()
        frontier.put(0, start_node)

        while not frontier.is_empty:
            current_node = frontier.get()

            if current_node == goal_node:  # early exit
                break

            for new_node in self._reachable_neighbors(current_node):
                new_cost = cost_so_far[current_node] + self.cost(current_node, new_node)
                if (
                    new_node not in came_from or new_cost < cost_so_far[new_node]
                    # add new_node to frontier if cheaper
                ):
                    cost_so_far[new_node] = new_cost
                    frontier.put(priority=new_cost, node=new_node)
                    came_from[new_node] = current_node

        return came_from

    def route(
        self,
        from_node: IntVector2,
        to_node: IntVector2,
        algorithm: str = "UNIFORM_COST_SEARCH",
    ) -> list[IntVector2] | None:
        """Return a node-based route from `from_node` to `to_node`.

        Returns:
        --------
        `list[IntVector2]`:
            Nodes on the route `to_node`.
            Includes `to_node`; doesn't include `from_node`.

        `None`:
            if no route was found.

        """
        if algorithm != "UNIFORM_COST_SEARCH":
            err_msg = f"Algorithm {algorithm} not implemented."
            raise NotImplementedError(err_msg)

        came_from = self._search(from_node, to_node)

        # Construct node path starting at `to_node` and retracing toward `from_node`...
        path_from_goal = [to_node]
        current_node = to_node

        while current_node != from_node:
            came_from_node = came_from.get(current_node)
            if came_from_node is None:
                return None

            current_node = came_from_node
            path_from_goal.append(current_node)

        return list(reversed(path_from_goal))
