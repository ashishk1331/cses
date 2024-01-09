n = int(input())
# n = 10

count = 0
while n > 0:
	temp = n//5
	count += temp
	n = temp
print(count)