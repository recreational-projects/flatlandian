"""Tests for `NavigationGrid` class."""

from flatlandian.int_vector2 import IntVector2
from flatlandian.navigation_grid import NavigationGrid


def test_create() -> None:
    # arrange
    # act
    ng = NavigationGrid(IntVector2(2, 2))
    # assert
    assert ng.nodes == {
        IntVector2(0, 0),
        IntVector2(0, 1),
        IntVector2(1, 0),
        IntVector2(1, 1),
    }
    assert isinstance(ng.nodes, frozenset)
    assert ng.blocked_nodes == set()
