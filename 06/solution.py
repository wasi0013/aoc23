from math import ceil, prod

time, distance = open("input.txt", "r").readlines()
time = list(map(int, time[5:].split()))
distance = list(map(int, distance[9:].split()))
total_time = int("".join(f"{i}" for i in time))
total_distance = int("".join(f"{i}" for i in distance))

def score_count(t, d): 
    return sum(tt * (t - tt) > d for tt in range(ceil(d/t) + ceil(d/t)//5, t//2 + 1)) * 2 - (t%2==0)

r1 = prod(score_count(t, d) for t, d in zip(time, distance))
r2 = score_count(total_time, total_distance)
print(r1, r2)