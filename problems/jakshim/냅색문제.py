def solution():
    n, m = map(int, input().split())
    w = list(map(int, input().split()))
    
    dp = [[0] * (m+1) for _ in range(n+1)]
    dp[0][0] = 1
    for i in range(1, n+1):
        object_weight = w[i-1]
        for possible_weight in range(m+1):
            dp[i][possible_weight] = dp[i-1][possible_weight]

            if possible_weight >= object_weight:
                dp[i][possible_weight] += dp[i-1][possible_weight - object_weight]
    
    return sum(dp[n])

if __name__ == "__main__":
    print(solution())  
