n, x = list(map(int, input().split()))
array = list(map(int, input().split()))

# n, x = 5, 7
# array = [2, 4, 1, 2, 7]

i = j = count = mus = 0

while j < n:
	if mus > x:
		while mus > x:
			mus -= array[i]
			i += 1
	else:
		mus += array[j]
		j += 1

	if mus == x:
		count += 1

while i < n:
	if mus == x:
		count += 1
	mus -= array[i]
	i += 1

print(count)