sequences = open("input.txt", "r").read().strip().split(",")
boxes = [[] for _ in range(256)]
fls = dict()

def hash(s, val=0):
    return val if not s else hash(s[1::], ((val + ord(s[0])) * 17) % 256)    

for step in sequences:
    if "=" in step:
        lbl = step.split("=")[0] 
        box, fls[lbl] = hash(lbl), int(step.split("=")[-1])
        if lbl in boxes[box]:
            index = boxes[box].index(lbl)
            boxes[box][index] = lbl
        else:
            boxes[box].append(lbl)
    if "-" in step:
        lbl = step[:-1]
        box = hash(lbl)
        if lbl in boxes[box]:
            boxes[box].remove(lbl)

def part1(): 
    return sum(map(hash, sequences))
def part2():
    return sum(i*j*fls[lbl] for i, b in enumerate(boxes, 1) for j, lbl in enumerate(b, 1))

print(part1(), part2())