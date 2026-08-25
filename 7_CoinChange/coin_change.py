def min_coins(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[amount] if dp[amount] != float('inf') else -1


def count_ways(coins, amount):
    dp = [0] * (amount + 1)
    dp[0] = 1
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] += dp[i - coin]
    return dp[amount]


if __name__ == "__main__":
    coins = [1, 2, 5]
    amount = 11
    print("Coins available:", coins)
    print("Target amount:", amount)
    print("Minimum coins needed:", min_coins(coins, amount))
    print("Number of ways to make the amount:", count_ways(coins, amount))
