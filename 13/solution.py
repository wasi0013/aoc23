grids = [g.split("\n") for g in open("input.txt", "r").read().strip().split("\n\n")]


def count_smudge(grid1, grid2):
    return sum(x != y for x, y in zip(grid1, grid2))


def add_up(g, num_of_smudge):
    return sum(
        [x, x * 100][i]
        for i, g in enumerate((list(zip(*g)), g))
        for x in range(1, len(g))
        if sum(count_smudge(g[x+i], g[x-i-1]) for i in range(min(x, len(g)-x)))
        == num_of_smudge
    )


def summarize(part2=False):
    return sum(add_up(grid, part2) for grid in grids)


print(summarize(), summarize(part2=True))
