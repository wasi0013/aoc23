from math import prod

r1, r2 = 0, 0
with open("input.txt", "r") as f:
    for line in f.readlines():
        d = {}
        text, data = line.split(":")
        num = int(text.split()[-1])
        records = map(
            lambda p: map(lambda t: t.split(), p),
            map(lambda s: s.split(","), data.split(";")),
        )
        sets = list(
            map(lambda cubes: map(lambda x: (int(x[0]), x[-1]), cubes), records)
        )
        for cubes in sets:
            for count, color in cubes:
                d[color] = max(d.get(color, 0), count)
        if d["red"] <= 12 and d["green"] <= 13 and d["blue"] <= 14:
            r1 += num
        r2 += prod(d.values())
print(r1, r2)
