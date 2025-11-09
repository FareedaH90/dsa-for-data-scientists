"""
Dynamic Programming (DP) Basics
Author: Fareeda Hamid
"""

# ------------------------------
# 1. Fibonacci / Climbing Stairs
# ------------------------------
def climb_stairs(n):
    """Return number of ways to climb n steps (1 or 2 each time)."""
    if n <= 2:
        return n
    a, b = 1, 2
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b

# ------------------------------
# 2. House Robber Problem
# ------------------------------
def house_robber(nums):
    """Max money without robbing adjacent houses."""
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    dp = [0] * len(nums)
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    for i in range(2, len(nums)):
        dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])
    return dp[-1]

# ------------------------------
# 3. Coin Change (Min coins)
# ------------------------------
def coin_change(coins, amount):
    """Return min number of coins to make up given amount."""
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for coin in coins:
        for x in range(coin, amount + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)
    return dp[amount] if dp[amount] != float('inf') else -1


if __name__ == "__main__":
    print("Climb Stairs:", climb_stairs(5))           # 8
    print("House Robber:", house_robber([2,7,9,3,1])) # 12
    print("Coin Change:", coin_change([1,2,5], 11))   # 3
