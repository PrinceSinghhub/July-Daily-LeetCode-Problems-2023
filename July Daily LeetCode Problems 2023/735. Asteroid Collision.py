class Solution(object):
    def asteroidCollision(self, asteroids):
        result = []
        for a in asteroids:
            result.append(a)
            while len(result) > 1 and result[-1] < 0 and result[-2] > 0:
                last = result.pop()
                if abs(last) == result[-1]:
                    result.pop()
                elif abs(last) > result[-1]:
                    result[-1] = last
        return result
