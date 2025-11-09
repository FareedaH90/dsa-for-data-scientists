"""
Arrays & Two-Pointers Patterns
Author: Fareeda Hamid
"""

# ------------------------------
# 1. Two-Pointers: Two Sum (sorted array)
# ------------------------------
def two_sum_sorted(nums, target):
    """Return indices of two numbers that sum to target (sorted array)."""
    l, r = 0, len(nums) - 1
    while l < r:
        s = nums[l] + nums[r]
        if s == target:
            return [l, r]
        elif s < target:
            l += 1
        else:
            r -= 1
    return []

# ------------------------------
# 2. Prefix Sum: Range Sum Query
# ------------------------------
def prefix_sum(nums):
    """Return prefix sum array."""
    pre = [0]
    for n in nums:
        pre.append(pre[-1] + n)
    return pre

def range_sum(pre, l, r):
    """Compute sum in nums[l:r] using prefix sums."""
    return pre[r] - pre[l]

# ------------------------------
# 3. Searching Extremes: Max & Min
# ------------------------------
def find_extremes(nums):
    """Return (min, max) of array."""
    min_val, max_val = nums[0], nums[0]
    for n in nums:
        min_val = min(min_val, n)
        max_val = max(max_val, n)
    return min_val, max_val


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    print("Two Sum Sorted:", two_sum_sorted(nums, 9))  # [0, 1]

    pre = prefix_sum([1, 2, 3, 4])
    print("Range Sum 1-3:", range_sum(pre, 1, 3))  # 5 (2+3)

    print("Extremes:", find_extremes([10, 3, 8, 15, 2]))
