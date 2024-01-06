schematic = []
digits = "0123456789"


def find_symbols(schematic):
    for i, row in enumerate(schematic):
        for j, c in enumerate(row):
            if c not in "0123456789.": 
                yield (i, j) 


def solve(schematic):
    seen, gears, numbers = set(), dict(), []
    for i, j in find_symbols(schematic):
        if (i, j) in seen: continue
        seen.add((i, j))
        for k in [-1, 0, 1]:
            for m in [-1, 0, 1]:
                if ((i + k, j + m) not in seen) and (schematic[i + k][j + m] in digits):
                    p, n, num = j + m, j + m, ""
                    while n < len(schematic[0]):
                        if schematic[i + k][n] not in digits: break
                        num += schematic[i + k][n]
                        seen.add((i + k, n))
                        n += 1
                    while p - 1 >= 0:
                        if schematic[i + k][p - 1] not in digits: break
                        num = schematic[i + k][p - 1] + num
                        seen.add((i + k, p - 1))
                        p -= 1
                    numbers.append(int(num))
                    if schematic[i][j] == "*":
                        gears[f"{i} {j}"] = gears.get(f"{i} {j}", [])
                        gears[f"{i} {j}"].append(int(num))
    r1, r2 = sum(numbers), sum(x[0] * x[1] for x in gears.values() if len(x) == 2)
    return r1, r2


with open("input.txt", "r") as f:
    for line in f.readlines():
        schematic.append([i for i in line.strip()])

r1, r2 = solve(schematic)
print(r1, r2)
