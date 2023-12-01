#!/usr/bin/python3

"""
island_perimeter module

This module defines a function to calculate the perimeter of the island described in a grid.

"""

def island_perimeter(grid):
    """
    Calculate the perimeter of the island in the given grid.

    Args:
    - grid (List[List[int]]): A list of lists representing the island grid.

    Returns:
    - int: The perimeter of the island.

    """
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])
    perimeter = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4  # Assume all sides are land

                # Check adjacent cells and subtract the shared sides
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2  # Subtract top side
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2  # Subtract left side

    return perimeter

# Example usage:
if __name__ == "__main__":
    grid = [
        [0, 1, 0, 0],
        [1, 1, 1, 0],
        [0, 1, 0, 0],
        [1, 1, 0, 0]
    ]

    result = island_perimeter(grid)
    print(result)
