class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        n=len(cookies)

        @cache
        def fn(mask,k):
            if mask==0:
                return 0

            if k==0:
                return inf

            ans=inf
            orig=mask

            while mask:
                mask=orig &(mask-1)
                res=sum(cookies[i] for i in range(n) if (orig^mask) & 1<<i)
                ans=min(ans,max(res,fn(mask,k-1)))

            return ans

        return fn((1<<n)-1,k)