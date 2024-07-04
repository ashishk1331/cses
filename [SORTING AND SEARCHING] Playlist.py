n = int(input())
array = list(map(int, input().split()))

# n = 8
# array = list(map(int, "1 2 1 3 2 7 4 2".split()))

i = j = 0
visited = set()

ans = 0

while j < n:

	if array[j] in visited:
		temp = 0
		while array[i] != array[j]:
			visited.remove(array[i])
			i += 1
		i += 1
	else:
		visited.add(array[j])
	j += 1

	ans = max(ans, j - i)

print(ans)