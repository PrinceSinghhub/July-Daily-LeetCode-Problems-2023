class Solution:
    def largestVariance(self, s: str) -> int:

        res = 0
        unique = set(s)
        for a in unique:
            for b in unique:
                var = 0
                has_b = False
                first_b = False
                for ch in s:
                    var += ch == a
                    if ch == b:
                        has_b = True
                        if first_b and var >= 0:
                            first_b = False
                        elif var < 0:
                            first_b = True
                            var = -1
                        else:
                            var -= 1
                    res = max(res, var if has_b else 0)
        return res

