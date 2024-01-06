from functools import reduce
import sys
from pprint import pprint as print

sys.setrecursionlimit(2350)

lines = open("input.txt", "r").readlines()
tiles = [list(x.strip()) for x in lines]
dirs = dict(zip(["R", "L", "D", "U"], [(0, 1), (0, -1), (1, 0), (-1, 0)]))
dir_map = {
    "|": {"R": ["D", "U"], "L": ["D", "U"], "D": ["D"], "U": ["U"]},
    "/": {"R": ["U"], "L": ["D"], "D": ["L"], "U": ["R"]},
    "\\": {"R": ["D"], "L": ["U"], "D": ["R"], "U": ["L"]},
    "-": {"R": ["R"], "L": ["L"], "D": ["L", "R"], "U": ["L", "R"]},
    ".": {"R": ["R"], "L": ["L"], "D": ["D"], "U": ["U"]},
}


def beam_it(x, y, direction, visited):
    if (x, y, direction) in visited:
        return
    visited.add((x, y, direction))
    for next_direction in dir_map[tiles[x][y]][direction]:
        nx, ny = x + dirs[next_direction][0], y + dirs[next_direction][1]
        if 0 <= nx < len(tiles) and 0 <= ny < len(tiles[0]):
            beam_it(nx, ny, next_direction, visited)


def energized(x, y, direction):
    visited = set()
    beam_it(x, y, direction, visited)
    return len(set([(x, y) for x, y, _ in visited]))

part1 = energized(0, 0, "R")
print(part1)

part2 = reduce(
    lambda r, x: max(
        r,
        energized(x, 0, "R"),
        energized(0, x, "D"),
        energized(x, 0, "L"),
        energized(0, x, "U"),
    ),
    range(len(tiles)),
    0,
)
print(part2)
