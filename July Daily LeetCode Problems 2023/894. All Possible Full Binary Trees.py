class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n % 2 == 0:
            return None

        dp = defaultdict(list)
        dp[1] = [TreeNode(0)]

        def dfs(k):
            if len(dp[k]) >= 1:
                return dp[k]
            temp = []
            for i in range(1, k, 2):
                left = dfs(i)
                right = dfs(k - 1 - i)
                # print(left, right)
                for a in left:
                    for b in right:
                        c = TreeNode(0)
                        c.left = a
                        c.right = b
                        temp.append(c)
            dp[k] = temp
            return temp
        return dfs(n)

