"""
Sliding Window & Two-Pointer Patterns
Author: Fareeda Hamid
"""

# ------------------------------
# 1. Fixed-Size Sliding Window
# ------------------------------
def max_subarray_sum(nums, k):
    """Find max sum of subarray of size k."""
    window_sum = sum(nums[:k])
    max_sum = window_sum
    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i - k]
        max_sum = max(max_sum, window_sum)
    return max_sum

# ------------------------------
# 2. Variable-Size Sliding Window
# ------------------------------
def longest_unique_substring(s):
    """Return length of longest substring without repeating chars."""
    seen, l, max_len = {}, 0, 0
    for r, ch in enumerate(s):
        if ch in seen and seen[ch] >= l:
            l = seen[ch] + 1
        seen[ch] = r
        max_len = max(max_len, r - l + 1)
    return max_len

# ------------------------------
# 3. Two-Pointers for Pair Sum
# ------------------------------
def has_pair_sum(nums, target):
    """Return True if array contains pair that sums to target."""
    nums.sort()
    l, r = 0, len(nums) - 1
    while l < r:
        s = nums[l] + nums[r]
        if s == target:
            return True
        elif s < target:
            l += 1
        else:
            r -= 1
    return False


if __name__ == "__main__":
    print("Max Subarray Sum:", max_subarray_sum([2, 1, 5, 1, 3, 2], 3))
    print("Longest Unique Substring:", longest_unique_substring("abcabcbb"))
    print("Pair Sum Exists:", has_pair_sum([1, 2, 3, 9], 8))
