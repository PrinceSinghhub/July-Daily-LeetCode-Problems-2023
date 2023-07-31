class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        lenth = len(weights)
        if k == 1 or k == lenth:
            return 0
        answer = 0
        ans = 0
        k -=1
        res = []
        for i in range(lenth - 1):
            res.append(weights[i] + weights[i+1])
        result = res.copy()
        res.sort(reverse=True)
        result.sort()
        for i in range(k):
            ans += res[i]
        for i in range(k):
            answer += result[i]
        return (ans - answer)