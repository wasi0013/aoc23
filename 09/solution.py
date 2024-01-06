data = list(map(lambda x: list(map(int, x.split())), open("input.txt", "r").readlines()))

def calc(seq):
	return seq[-1] + calc([seq[i+1]-seq[i] for i in range(len(seq)-1)]) if any(seq) else 0

def solve_p1(): return sum(map(calc, data))
def solve_p2():	return sum(calc(seq[::-1]) for seq in data)
	
print(solve_p1(), solve_p2())