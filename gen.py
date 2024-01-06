#!/usr/bin/env python3.12
import sys
import os
import requests

filename = "solution.py"
input_file = "input.txt"
day = sys.argv[1]
session = ""
print(f"Preparing Day {day}")
try:
    with open(".cli_env/session", "r") as f:
        session = f.read()
except Exception as _:
    print("Grab your session Cookie, and put in the .cli_env/session file.")
try:
    os.mkdir(day)
except Exception as _:
    pass

if not os.path.exists(os.path.join(day, filename)):
    with open(os.path.join(day, filename), "w") as f:
        f.write(f'lines = open("{input_file}", "r").readlines()\n')
else:
    print(f"{filename} already exists")

if not os.path.exists(os.path.join(day, input_file)):
    try:
        with open(os.path.join(day, input_file), "w") as f:
            url = f"https://adventofcode.com/2023/day/{day}/input"
            inputs = requests.get(url, headers={"Cookie": f"session={session}"}).text
            f.write(f"{inputs}")
    except Exception as e:
        print(e)
        sys.exit(0)
else:
    print(f"{input_file} already exists")

print("Updating README")

percentage = int(day) * 4
readme = f"""# <img src="https://adventofcode.com/favicon.png" width=24 alt=":star:"> Advent of Code 2023

[![AOC](https://img.shields.io/badge/solved-{percentage}%25-00cc00?labelColor=0f0f23)](https://adventofcode.com/2023/)

Advent of Code :snake: Python 3.12 Solutions.

<table>
<thead>
{"\n".join(f"    <th> <a href='https://adventofcode.com/2023/day/{d}'>{d}</a></th>" for d in range(1, 26))}
</thead>
<tbody>
<tr>
{"\n".join(f"    <td> <a href='{d:02}/{filename}'>🌟🌟</a></td>" for d in range(1, int(day) + 1))}
{"\n".join("    <td> <a href='#'>☆☆</a></td>" for d in range(1, 25 - int(day) + 1))}
</tr>
</tbody>
</table>
"""
with open("README.md", "w") as f:
    f.write(readme)
