n = int(input())
# n = 654321 # 113810539

dp = [0]*(n + 1)
dp[0] = 1

for i in range(1, n + 1):
	for j in [1, 2, 3, 4, 5, 6]:
		if i - j >= 0:
			dp[i] += dp[i - j]
			dp[i] = dp[i]%(10**9 + 7)

print(dp[n])