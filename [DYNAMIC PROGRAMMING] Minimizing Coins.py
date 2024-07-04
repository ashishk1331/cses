n, m = list(map(int, input().split()))
coins = list(map(int, input().split()))

# n, m = 3, 11
# coins = [1, 5, 7]

dp = [m + 1]*(m + 1)
dp[0] = 0

for i in range(1, m + 1):
	for j in coins:
		if i - j >= 0:
			dp[i] = min(dp[i], dp[i - j] + 1)

print(dp[m] if dp[m] != m + 1 else -1)