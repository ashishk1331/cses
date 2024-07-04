n = int(input())
array = list(map(int, input().split()))

# n = 8
# array = list(map(int, "2 5 1 4 8 3 2 5".split()))

n = len(array)
stack = []
res = [0]*n

for index, value in enumerate(array):

	while stack and array[stack[-1]] >= value:
		stack.pop()

	ans = stack[-1] + 1 if stack else 0
	print(ans, end= " ")

	stack.append(index)

print()