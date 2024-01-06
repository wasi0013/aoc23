from math import lcm
from itertools import cycle
from re import findall

commands, _, *lines = open("input.txt", "r").readlines()
d = dict((key, (node1, node2)) for (key, node1, node2) in map(lambda line: findall(r"[A-Z]+", line), lines))                    

def solve_p1():
    key = "AAA"
    for i, command in enumerate(cycle(commands.strip()), 1):
        key = d[key][command == "R"]
        if key == "ZZZ":
            return i

def solve_p2():
    results = []
    for key in [i for i in d.keys() if i.endswith("A")]:
        for i, command in enumerate(cycle(commands.strip()), 1):
            key = d[key][command == "R"]
            if key.endswith("Z"):
                results.append(i)
                break
    return lcm(*results)

print(solve_p1(), solve_p2())