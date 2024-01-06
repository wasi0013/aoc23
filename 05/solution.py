from itertools import count
def track(values, seed):
    for val in values:
        dest, source, inc = val
        if source <= seed < source + inc:
            return dest + abs(source - seed)
    return seed

def solve_part1(maps, seeds, keys):
    locations = []
    for seed in seeds:
        for key in keys:
            values = maps.get(key)
            seed = track(values, seed)
        locations.append(seed)
    return min(locations)

def backtrack(values, loc):
    for val in values:
        dest, source, inc = val
        if dest <= loc < dest + inc:
            return source + abs(dest - loc)
    return loc

def solve_part2(maps, seeds, keys):
    for location in count():
        seed = location
        for key in keys[::-1]:
            values = maps.get(key)
            seed = backtrack(values, seed)
        for s1, s2 in zip(seeds[::2], seeds[1::2]):
            if s1 <= seed < s1 + s2 :
                return location

def parse(lines):
    maps = dict()
    key = ''
    for line in lines:
        values = line.split()
        if ":" in line:
            key = values[0]
        elif len(values) == 3:
            maps[key] = maps.get(key, [])
            maps[key].append(list(map(int, values)))
    return maps


keys = ['seed-to-soil', 'soil-to-fertilizer', 'fertilizer-to-water', 'water-to-light', 'light-to-temperature', 'temperature-to-humidity', 'humidity-to-location']
first, *lines = open("input.txt", "r").readlines()
seeds = list(map(int, first[7:].split()))
maps = parse(lines)

print(solve_part1(maps, seeds, keys))
print(solve_part2(maps, seeds, keys))
