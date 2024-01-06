from collections import Counter
cards = list(map(lambda x: x.split(), open("input.txt", "r").readlines()))
def get_score(c): 
    return [(1,1,1,1,1),(1,1,1,2),(1,2,2),(1,1,3),(2,3),(1,4),(5,)].index(tuple(sorted(c.values())))

def solve_p1(card):
    return (get_score(Counter(card)),*("23456789TJQKA".find(i) for i in card))
    
def solve_p2(card):
    c = Counter(card)
    j = c['J']
    if j == 5:
        c["A"] = 5
        del c['J']
    elif j > 0:    
        del c['J']
        c[c.most_common()[0][0]] += j
    return (get_score(c), *("J23456789TQKA".find(i) for i in card), j > 0)

def run(f):
    s = sorted(cards, key=lambda x: f(x[0]))
    return sum([int(point) * c for c, (card, point) in enumerate(s, 1)])

print(run(solve_p1), run(solve_p2))
