# n | 이친수 
# 1   1 -> 1개
# 2   10 -> 1개
# 3   100 101 -> 2개
# 4   1000 1001 1010 -> 3개
# 5   10000 10001 10010 10100 10101 -> 5개
# 6   100000 100001 100010 100100 101000 100101 101001 101010 -> 8개
# 점화식 dp(n) = dp(n-2) + dp(n-1)

dp = [1,1,2]
n = int(input())
for i in range(3,n):
    dp.append(dp[i-2]+dp[i-1])
print(dp[-1])