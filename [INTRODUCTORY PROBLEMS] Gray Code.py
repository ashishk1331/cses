n = int(input())
# n = 3

arr = ["0", "1"]

while n > 1:
	temp = ["1" + x for x in arr[::-1]]
	arr = ["0" + x for x in arr]
	arr.extend(temp)
	n -= 1

for i in arr:
	print(i)