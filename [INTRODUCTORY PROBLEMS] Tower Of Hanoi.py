# n = int(input())
n = 3

res = []

def tower(n, A, C, B):
	if n:
		tower(n - 1, A, B, C)
		res.append((A, C))
		tower(n - 1, B, C, A)

tower(n, 1, 3, 2)

print(res)