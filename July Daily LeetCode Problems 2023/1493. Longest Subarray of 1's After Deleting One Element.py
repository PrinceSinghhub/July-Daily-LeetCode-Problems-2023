class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        k1=0
        k0=0
        k2=0
        l=[]
        if nums.count(0) == 0:
            return len(nums)-1
        for i in range(len(nums)):
            if nums[i] == 1:
                if k0!=0:
                    k1+=1
                    k2+=1
                else:
                    k1+=1
            else:
                k0+=1
                if k0%2 == 0:
                    l.append(k1)
                    k1=0
                else:
                    l.append(k2)
                    k2=0
        l.append(k1)
        l.append(k2)
        return max(l)