from collections import defaultdict


class Solution:
    def longestSubsequence(self, arr: List[int], dif: int) -> int:
        lengths = defaultdict(lambda: 0)

        for num in arr:
            lengths[num] = lengths[num - dif] + 1

        return max(lengths.values())