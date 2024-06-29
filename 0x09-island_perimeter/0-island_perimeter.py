#!/usr/bin/python3
"""
	island perimeter
"""


def connet(grid, row, col, conet):
    """return connetion"""
    if row:
        if grid[row - 1][col]:
            conet += 1
    if row != len(grid) - 1:
        if grid[row + 1][col]:
            conet += 1
    if col:
        if grid[row][col - 1]:
            conet += 1
    if col != len(grid[row]) - 1:
        if grid[row][col + 1]:
            conet += 1
    return (conet)


def island_perimeter(grid):
    """island_perimeter"""
    count = 0

    for row in range(len(grid)):
        for col in range(len(grid[row])):
            conet = 0
            conet = connet(grid, row, col, conet)
            if grid[row][col]:
                count += (4 - conet)
                if conet == 0:
                    return (count)
            else:
                if conet == 4:
                    return (0)
    return (count)
