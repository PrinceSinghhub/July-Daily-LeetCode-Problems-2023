class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courseGraph = [[] for _ in range(numCourses)]
        for ai, bi in prerequisites:
            courseGraph[ai].append(bi)

        visited = [False] * numCourses
        stack = defaultdict(bool)
        for c in range(numCourses):
            if not self.process(c, courseGraph, visited, stack):
                return False
        return True

    def process(self, c, courseGraph, visited, stack):

        if stack[c]:
            return False
        stack[c] = True
        for prereq in courseGraph[c]:
            if visited[prereq] == True:
                continue
            if not self.process(prereq, courseGraph, visited, stack):
                return False
        stack[c] = False
        visited[c] = True
        return True