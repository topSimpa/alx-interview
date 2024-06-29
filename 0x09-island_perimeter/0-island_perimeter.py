#!/usr/bin/python3
"""
	island perimeter
"""

def island_perimeter(grid):
    """island_perimeter"""
    hold_col = 0
    count = 0

    for row in range(1, len(grid) - 1):
        col = hold_col
        while (col < len(grid)):
            if ((grid[row][col] == 1) and (hold_col == 0)):
                hold_col = col
            if (grid[row][col] == 1):
                count += 1
            elif ((hold_col != 0) and (grid[row][col] == 0)):
                break
            col += 1
    result = (count - 2) * 2 + 6
    return (result)
