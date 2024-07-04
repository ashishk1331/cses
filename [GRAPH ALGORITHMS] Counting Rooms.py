from collections import deque

n, m = list(map(int, input().split()))
grid = []

for _ in range(n):
	grid.append([x for x in input()])

# n, m = 5, 8
# grid = [
# 	['#', '#', '#', '#', '#', '#', '#', '#'], 
# 	['#', '.', '.', '#', '.', '.', '.', '#'], 
# 	['#', '#', '#', '#', '.', '#', '.', '#'], 
# 	['#', '.', '.', '#', '.', '.', '.', '#'], 
# 	['#', '#', '#', '#', '#', '#', '#', '#']
# ]

directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def bfs(r, c):
	q = deque([(r, c)])

	while q:
		for _ in range(len(q)):
			r, c = q.popleft()
			grid[r][c] = "#"

			for dx, dy in directions:
				x, y = r + dx, c + dy
				if (
					x in range(n) and 
					y in range(m) and
					grid[x][y] == '.'
				):
					q.append((x, y))


count = 0
for i in range(n):
	for j in range(m):
		if grid[i][j] == ".":
			bfs(i, j)
			count += 1

print(count)