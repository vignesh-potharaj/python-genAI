def sort_scores(scores):
    n = len(scores)
    swaps = 0
    leaderboard = scores[:]
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if leaderboard[j] < leaderboard[j + 1]:
                leaderboard[j], leaderboard[j + 1] = leaderboard[j + 1], leaderboard[j]
                swaps += 1
                
    return leaderboard, swaps

scores = [300, 150, 400, 250, 100]
print(sort_scores(scores))
