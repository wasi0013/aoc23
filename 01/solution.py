import re

with open("input.txt", "r") as f:
    lines = f.readlines()


def find(string, reverse=False):
    string = string.lower()
    d = dict((i, int(i)) for i in "0123456789")
    for i, j in enumerate(
        ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    ):
        if reverse:
            j = j[::-1]
        d[j] = i
    if reverse:
        string = string[::-1]
    indexes = [(string.find(i), d[i]) for i in d.keys() if string.find(i) != -1]
    _, digit = min(indexes, key=lambda x: x[0])
    return digit


r1 = sum(
    map(lambda x: int(f"{re.findall(r'\d', x)[0]}{re.findall(r'\d', x)[-1]}"), lines)
)
r2 = sum(map(lambda line: find(line) * 10 + find(line, True), lines))
print(r1, r2)
