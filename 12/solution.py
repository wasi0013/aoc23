from functools import lru_cache


def parse(x=1):
    return [
        ("?".join([line.split()[0]] * x), tuple(map(int, line.split()[-1].split(","))) * x)
        for line in open("input.txt", "r").readlines()
    ]


@lru_cache
def count(s, c):
    if not c: return "#" not in s
    if not s: return len(c) == 0
    dmg = (
        s[0] in "#?"
        and c[0] <= len(s)
        and "." not in s[: c[0]]
        and (c[0] == len(s) or s[c[0]] != "#")
    )
    return (s[0] in ".?" and count(s[1:], c) or 0) + (
        dmg and count(s[c[0] + 1 :], c[1:]) or 0
    )


r1 = sum(count(s, c) for s, c in parse())
r2 = sum(count(s, c) for s, c in parse(5))

print(r1, r2)
