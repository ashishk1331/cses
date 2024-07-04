# from rich import print

# text = """5 8
# ########
# #.A#...#
# #.##.#B#
# #......#
# ########""".split("\n")

# n, m = list(map(int, text.pop(0).split()))
# grid = []
# for line in text:
# 	grid.append([x for x in line])

n, m = list(map(int, input().split()))
grid = []
for line in range(n):
	grid.append([x for x in input()])

directions = [(1, 0, "D"), (-1, 0, "U"), (0, 1, "R"), (0, -1, "L")]
paths = []
visited = set()
def dfs(r, c, path):
	if (
		r not in range(n) or
		c not in range(m) or
		(r, c) in visited or
		grid[r][c] == "#"
	):
		return


	if grid[r][c] == "B":
		return paths.append(path)

	visited.add((r, c))
	for dx, dy, step in directions:
		dfs(r + dx, c + dy, path + step)
	visited.remove((r, c))


for i in range(n):
	for j in range(m):
		if grid[i][j] == "A":
			dfs(i, j, "")
			break

if paths:
	print("YES")
	min_path = min(paths)
	print(len(min_path))
	print(min_path)
else:
	print("NO")