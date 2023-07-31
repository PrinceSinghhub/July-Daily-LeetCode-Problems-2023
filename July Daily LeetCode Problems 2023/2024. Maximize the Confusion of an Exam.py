class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        maxf=0
        ans=0
        count=collections.Counter()
        n=len(answerKey)
        for i in range(n):
            count[answerKey[i]]+=1
            maxf=max(maxf,count[answerKey[i]])
            if ans-maxf<k:
                ans+=1

            else:
                count[answerKey[i-ans]]-=1

        return ans