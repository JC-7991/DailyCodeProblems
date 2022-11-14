def findMaxSum(arr, N):
 
    dp = [[0 for i in range(2)] for j in range(N)]
     
    if (N == 1):
        return arr[0]

    dp[0][0] = 0
    dp[0][1] = arr[0]
   
    for i in range(1, N):
        dp[i][1] = dp[i - 1][0] + arr[i]
        dp[i][0] = max(dp[i - 1][1], dp[i - 1][0])
   
    return max(dp[N - 1][0], dp[N - 1][1])
 
arr = [5, 5, 10, 100, 10, 5]
N = len(arr)
print(findMaxSum(arr, N))