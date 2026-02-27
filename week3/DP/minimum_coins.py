def min_coins(n, memo):
    if n == 0:
        return 0
    if n < 0:
        return float('inf')
    
    if memo[n] != -1:
        return memo[n]
    
    take1 = min_coins(n - 1, memo)
    take2 = min_coins(n - 2, memo)
    take5 = min_coins(n - 5, memo)
    
    memo[n] = 1 + min(take1, take2, take5)
    return memo[n]


# Input
n = int(input())
memo = [-1] * (n + 1)

print(min_coins(n, memo))