#!/usr/bin/python3

def makeChange(coins, total):
    if total <= 0:
        return 0

    # Initialize a list to store the minimum number of coins needed for each amount
    # Initialize with a value greater than any possible result
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Zero coins needed to make a total of 0

    # Iterate over each coin and update the dp array
    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # If dp[total] is still float('inf'), it means the total cannot be reached
    return dp[total] if dp[total] != float('inf') else -1

# Test cases
print(makeChange([1, 2, 25], 37))   # Output: 7
print(makeChange([1256, 54, 48, 16, 102], 1453))   # Output: -1
