from collections import deque


class Solution:

    def mapWithParentNode(self, node, parentNode, hasmap):

        if node == None:
            return

        hasmap[node] = parentNode

        self.mapWithParentNode(node.left, node, hasmap)  # build for left subtree
        self.mapWithParentNode(node.right, node, hasmap)  # build for right subtree

    def bfs(self, startNode, K, hasmap):
        ans = []
        queue = deque()
        queue.append([startNode, 0])

        visited = set()

        while len(queue) != 0:
            data = queue.popleft()
            Node = data[0]
            distance = data[1]

            if Node not in visited:
                if distance == K:
                    ans.append(Node.val)
                    continue

                visited.add(Node)

                if Node.left:
                    queue.append([Node.left, distance + 1])

                if Node.right:
                    queue.append([Node.right, distance + 1])

                print(hasmap[Node])

                # for traversa in upword direction or for ParentNode
                if hasmap[Node]:
                    queue.append([hasmap[Node], distance + 1])

        return ans

    def distanceK(self, root, target, K):

        hasmap = {}
        self.mapWithParentNode(root, None, hasmap)

        print(hasmap)

        ans = self.bfs(target, K, hasmap)
        return ans


