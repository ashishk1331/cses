n = int(input())
arr = list(map(int, input().split()))

corrections = 0
for i in range(len(arr) - 1):
	diff = arr[i] - arr[i+1]
	if diff > 0:
		corrections += diff
		arr[i + 1] += diff

print(corrections)