import sys

grid = open("input.txt", "r").readlines()
sys.setrecursionlimit(len(grid) * len(grid[0]))
directions = {
    "right": {"x": 0, "y": 1, "symbols": "7J-"},
    "down": {"x": 1, "y": 0, "symbols": "LJ|"},
    "left": {"x": 0, "y": -1, "symbols": "LF-"},
    "up": {"x": -1, "y": 0, "symbols": "7F|"},
}

def change_direction(direction, symbol):
    match direction, symbol:
        case "right", "-": return "right"
        case "left", "-":  return "left"
        case "down", "|":  return "down"
        case "up", "|":    return "up"
        case "down", "L":  return "right"
        case "up", "7":    return "left"
        case "right", "7": return "down"
        case "right", "J": return "up"
        case "up", "F":    return "right"
        case "down", "J":  return "left"
        case "left", "F":  return "down"
        case "left", "L":  return "up"

def is_valid(x, y):
    return x >= 0 and x <= len(grid) and y >= 0 and y <= len(grid[0])

def get_coordinates(grid, start_symbol="S"):
    for i, line in enumerate(grid):
        if start_symbol in line:
            return (i, line.find(start_symbol))

def get_directions(grid):
    return [
        key
        for key in directions.keys()
        if is_valid(x + directions[key]["x"], y + directions[key]["y"])
        and grid[x + directions[key]["x"]][y + directions[key]["y"]]
        in directions[key]["symbols"]
    ]

x, y = get_coordinates(grid)
starting_directions = get_directions(grid)

matrix = [[0] * len(grid[0]) for _ in range(len(grid))]
matrix[x][y] = 1

def walk(p, q, direction, count):
    if (x, y) == (p, q):
        return count // 2
    matrix[p][q] = 1
    direction = change_direction(direction, grid[p][q])
    return walk(p + directions[direction]["x"], q + directions[direction]["y"], direction, count + 1)

def count_tiles():
    tiles_count = 0
    for i in range(len(grid)):
        is_tile = False
        for j in range(len(grid[0])):
            if matrix[i][j] and (
                grid[i][j] in directions["down"]["symbols"]
                or (grid[i][j] == "S" and "up" in starting_directions)
            ):
                is_tile = not is_tile
            tiles_count += is_tile and not matrix[i][j]
    return tiles_count

def solve_part1():
    direction = starting_directions[0]
    p, q = x + directions[direction]["x"], y + directions[direction]["y"]
    return walk(p, q, direction, 1)

def solve_part2(): 
    return count_tiles()

print(f"Part 1: {solve_part1()}")
print(f"Part 2: {solve_part2()}")
