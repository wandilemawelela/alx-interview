#!/usr/bin/python3
"""
Island module
"""


def island_perimeter(grid):
    """
    Returns the perimeter of the island described
    in grid.
    """
    if not grid or not grid[0]:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                # Each land cell has 4 potential
                # sides contributing to the perimeter
                perimeter += 4

                # Check if the cell above is land
                if r > 0 and grid[r - 1][c] == 1:
                    perimeter -= 2

                # Check if the cell to the left is land
                if c > 0 and grid[r][c - 1] == 1:
                    perimeter -= 2

    return perimeter
