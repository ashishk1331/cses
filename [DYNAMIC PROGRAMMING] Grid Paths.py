n = int(input())

grid = []

for _ in range(n):
	grid.append([x for x in input()])

# grid = [['.', '.', '.', '.'], ['.', '*', '.', '.'], ['.', '.', '.', '*'], ['*', '.', '.', '.']]
# n = 4

# def recur(r, c):
# 	if r == n - 1 and c == n - 1:
# 		return 1

# 	if (
# 		r not in range(n) or
# 		c not in range(n) or
# 		grid[r][c] == "*"
# 	):
# 		return 0

# 	return recur(r + 1, c) + recur(r, c + 1)

# ways = recur(0, 0)
# print(ways%(10**9 + 7))

dp = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
	if grid[0][i] == "*":
		break
	dp[0][i] = 1

for j in range(n):
	if grid[j][0] == "*":
		break
	dp[j][0] = 1

for i in range(1, n):
	for j in range(1, n):
		if grid[i][j] != "*":
			dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

print(dp[n - 1][n - 1]%(10**9 + 7))

grid
def recur(r, c, count):