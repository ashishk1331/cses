# n, x = list(map(int, input().split()))
# array = list(map(int, input().split()))

n, x = 5, 7
array = [2, -1, 3, 5, -2, 1, -1]

def recur(array, i, j):
	count = mus = 0

	while j < n:
		while mus > x:
			mus -= array[i]
			count += recur(array, i, j)
			i += 1

		if mus == x:
			count += 1
		
		mus += array[j]
		j += 1


	while i < n:
		if mus == x:
			count += 1
		mus -= array[i]
		i += 1
		
	return count

print(recur(array, 0, 0))