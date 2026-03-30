def knapsack(weights, values, capacity):
    n = len(weights)

    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(
                    dp[i - 1][w],  
                    values[i - 1] + dp[i - 1][w - weights[i - 1]]  
                )
            else:
                dp[i][w] = dp[i - 1][w]

    chosen_items = []
    w = capacity

    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            chosen_items.append(i)  # item number (1-based index)
            w -= weights[i - 1]

    chosen_items.reverse()

    return dp[n][capacity], chosen_items


weights = [1, 2, 3, 5]
values = [1, 6, 10, 16]
capacity = 7

max_value, items = knapsack(weights, values, capacity)

print("max value:", max_value)
print("items chosen:", items)

for item in items:
    print(f"Item {item}: weight={weights[item-1]}, value={values[item-1]}")