inputs = open("input.txt", "r").readlines()


def calc(grid, t=0):
    return sum(
        [0, i + (t := (t + 1))][c.strip() == "O"]
        for i, chunk in enumerate(grid[::-1])
        for c in sorted(chunk)
    )


print(
    sum(
        [
            calc(line)
            for line in list(map(lambda x: "".join(x).split("#"), zip(*inputs)))
        ]
    )
)

grid = tuple(map(lambda x: x.strip(), inputs))
total_cycles = 1000000000
cycles = [grid]


def slide_nwse(grid):
    for _ in range(4):
        grid = tuple(
            "#".join("".join(sorted(c, reverse=True)) for c in chunk.split("#"))
            for chunk in tuple(map("".join, zip(*grid)))[::-1]
        )
        grid = tuple(
            [
                "".join(row[::-1])
                for row in zip(*tuple(map(lambda x: "".join(x[::-1]), zip(*grid))))
            ]
        )

    return grid


for i in range(total_cycles):
    if (grid := slide_nwse(grid)) in cycles:
        break
    cycles.append(grid)

print(
    sum(
        s.count("O") * (len(grid) - j)
        for j, s in enumerate(
            cycles[
                cycles.index(grid)
                + (total_cycles - cycles.index(grid)) % (i + 1 - cycles.index(grid))
            ]
        )
    )
)