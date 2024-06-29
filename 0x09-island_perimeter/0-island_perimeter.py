#!/usr/bin/python3
"""
	island perimeter
"""


def island_perimeter(grid):
    """island_perimeter"""
    hold_col = 0
    count = 0

    if ((sum(grid[0]) != 0) or (sum(grid[-1]) != 0)):
        return (0)

    for row in range(0, len(grid)):
        col = hold_col
        while (col < len(grid[row])):
            if ((grid[row][col] == 1) and (hold_col == 0)):
                hold_col = col
            if (grid[row][col] == 1):
                count += 1
            elif ((hold_col != 0) and (grid[row][col] == 0)):
                break
            col += 1
    if count == 0:
        return (0)

    return (((count - 2) * 2) + 6)
