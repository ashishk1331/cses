# n = int(input())

# slots = []
# for _ in range(n):
# 	slots.append(list(map(int, input().split())))

with open("input.txt", "r") as file:
	data = file.read().split("\n")

n = int(data.pop(0))
slots = (tuple(map(int, each.split())) for each in data if len(each))

# n = 3
# slots = [(5, 8), (2, 4), (3, 9)]

cc = {}

for x, y in slots:
	cc[x] = cc[y] = 0

for index, key in enumerate(sorted(cc.keys()), 1):
	cc[key] = index

array = [0]*(len(cc) + 1)
for x, y in slots:
	array[cc[x]] += 1
	array[cc[y]] -= 1

for i in range(1, len(cc)):
	array[i] += array[i - 1]

print(max(array))