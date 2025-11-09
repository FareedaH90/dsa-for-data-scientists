"""
Hash Maps / Dictionaries Patterns
Author: Fareeda Hamid
"""

# ------------------------------
# 1. Two Sum using Hash Map
# ------------------------------
def two_sum(nums, target):
    """Return indices of two numbers that sum to target."""
    seen = {}
    for i, n in enumerate(nums):
        if target - n in seen:
            return [seen[target - n], i]
        seen[n] = i
    return []

# ------------------------------
# 2. Frequency Counter
# ------------------------------
def frequency_count(s):
    """Return frequency of each character in string."""
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    return freq

# ------------------------------
# 3. Prefix Sum with Hash Map (Subarray Sum Equals K)
# ------------------------------
def subarray_sum(nums, k):
    """Return number of subarrays that sum to k."""
    prefix = {0: 1}
    s = res = 0
    for n in nums:
        s += n
        res += prefix.get(s - k, 0)
        prefix[s] = prefix.get(s, 0) + 1
    return res


if __name__ == "__main__":
    print("Two Sum:", two_sum([2, 7, 11, 15], 9))
    print("Frequency Count:", frequency_count("datascience"))
    print("Subarray Sum Equals K:", subarray_sum([1, 2, 3], 3))
