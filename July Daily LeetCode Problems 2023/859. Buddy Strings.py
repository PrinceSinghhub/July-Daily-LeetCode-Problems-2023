class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:

        if len(s) != len(goal):
            return False

        c1, c2 = Counter(s), Counter(goal)
        print(c1, c2)
        if c1 != c2:
            return False

        diff = sum(1 for c1, c2 in zip(s, goal) if c1 != c2)
        print(diff)

        if diff > 2:
            return False

        if diff == 0 and max(c1.values()) == 1:
            return False
        return True