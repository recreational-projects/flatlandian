"""Tests for `Grid` class."""

from flatlandian.grid import Grid
from flatlandian.int_vector2 import IntVector2


def test_create() -> None:
    # arrange
    # act
    grid = Grid(IntVector2(2, 2))
    # assert
    assert grid.cells == {
        IntVector2(0, 0),
        IntVector2(0, 1),
        IntVector2(1, 0),
        IntVector2(1, 1),
    }
    assert isinstance(grid.cells, frozenset)


def test_neighbors() -> None:
    # arrange
    grid = Grid(IntVector2(3, 3))
    # act
    ns = grid.neighbors(IntVector2(1, 1))
    # assert
    assert len(ns) == 8
    assert ns == {
        IntVector2(0, 0),
        IntVector2(0, 1),
        IntVector2(0, 2),
        IntVector2(1, 0),
        IntVector2(1, 2),
        IntVector2(2, 0),
        IntVector2(2, 1),
        IntVector2(2, 2),
    }


def test_neighbors_corner_cell() -> None:
    # arrange
    grid = Grid(IntVector2(2, 2))
    # act
    ns = grid.neighbors(IntVector2(0, 0))
    # assert
    assert ns == {
        IntVector2(0, 1),
        IntVector2(1, 0),
        IntVector2(1, 1),
    }
