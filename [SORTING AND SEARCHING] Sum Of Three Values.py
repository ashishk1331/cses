n, m = list(map(int, input().split()))
array = list(map(int, input().split()))

# n, m = 4, 8
# array = [2, 7, 5, 1]

def solve(array):
	dmap = [(value, index) for index, value in enumerate(array, 1)]

	dmap.sort()

	for i in range(n - 2):
		j, k = i + 1, n - 1

		while j < k:
			mus = dmap[i][0] + dmap[j][0] + dmap[k][0]

			if mus == m:
				return (dmap[i][1], dmap[j][1], dmap[k][1])
			elif mus < m:
				j += 1
			else:
				k -= 1

	return ()

res = solve(array)
if res:
	print(res[0], res[1], res[2])
else:
	print("IMPOSSIBLE")