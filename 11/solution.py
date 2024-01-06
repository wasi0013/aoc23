lines = open("input.txt", "r").readlines()

def manhattan_distance_sum(galaxies):
    return sum(
    abs(galaxies[x][0] - galaxies[y][0]) + abs(galaxies[x][1] - galaxies[y][1])
    for x in range(len(galaxies))
    for y in range(x + 1, len(galaxies))
    )

v_expansion = "".join(
    map(lambda x: x * 2 if "#" not in x else x, lines)
)
v_expansion = list(zip(*v_expansion.splitlines()))
h_expansion = []
for i in v_expansion:
    if "#" not in i:
        h_expansion.append(i)
    h_expansion.append(i)

space = h_expansion
galaxies = list()

w, h = len(space), len(space[0])
for i in range(w * h):
    x, y = i // h, i % h
    if space[x][y] == "#":
        if (x, y) not in galaxies:
            galaxies.append((x, y))

r1 = manhattan_distance_sum(galaxies)


empty_h = [i for i, line in enumerate(lines) if "#" not in line]
empty_v = [i for i, row in enumerate(list(zip(*lines))) if "#" not in row]
empty_v.pop() # remove new lines
multiplier  = 1000000 - 1

g = []
i = 0
for x in range(len(lines)):
    i += x in empty_h
    j = 0
    for y in range(len(lines[0])):
        j += y in empty_v 
        if lines[x][y] == "#":
            p, q = x + multiplier * i, y + multiplier * j
            if (p, q) not in g:
                g.append((p, q))

r2 = manhattan_distance_sum(g)
print(r1, r2)