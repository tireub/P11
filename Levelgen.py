import numpy
from numpy.random import random_integers as random


def randmaze(width=29, height=29):
    # Initialize grid, all 0
    Grid = numpy.zeros((height, width), dtype=bool)
    elements = int((width // 2 + 1) * (height // 2 + 1))
    # Using recursive bactracking algorythm
    # Only the cells with even coordinates are to be visited

    # Find a starting point
    x, y = random(0, width // 2) * 2, random(0, height // 2) * 2
    # Switch it to 1

    visited = []
    stack = []
    Grid[x, y] = 1
    visited.append((x, y))

    while len(visited) < elements:
        neighbours = []
        # Determine valid neighbours
        if x > 1:
            if not (Grid[x-2, y]):
                neighbours.append((x - 2, y))
        if x < height - 2:
            if not (Grid[x + 2, y]):
                neighbours.append((x + 2, y))
        if y > 1:
            if not (Grid[x, y - 2]):
                neighbours.append((x, y - 2))
        if y < width - 2:
            if not (Grid[x, y + 2]):
                neighbours.append((x, y + 2))

        # if the cell has any unvisited neighbours
        if len(neighbours):
            # choose one of them randomly
            u, v = neighbours[random(0, len(neighbours) - 1)]

            # add current cell to the stack
            stack.append((x, y))

            # remove wall between current cell and chosen cell
            Grid[v + (y - v) // 2, u + (x - u) // 2] = 1

            # make chosen cell current and add it to visited
            x, y = u, v
            Grid[x, y] = 1
            visited.append((x, y))

        else:
            if len(stack):
                # get last cell from the stack
                x, y = stack[-1]

                # remove it from the stack
                del stack[-1]

    start = visited[0]
    finish = visited[-1]

    return (Grid, start, finish)
