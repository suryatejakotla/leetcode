class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        # The idea is that we find paths for both start and target nodes.
        # Once we have found them we reduce paths to a lowest common parent node.
        # We change the all items in path of start to 'U' and keep the path of target same.
        def dfs(node, target, path):
            if not node:
                return False

            if node.val == target:
                return True

            if node.left:
                if dfs(node.left, target, path):
                    path.appendleft('L')
                    return True

            if node.right:
                if dfs(node.right, target, path):
                    path.appendleft('R')
                    return True                
            
        s_path, t_path = deque(), deque()
        dfs(root, startValue, s_path)
        dfs(root, destValue, t_path)
        
        while s_path and t_path and s_path[0] == t_path[0]:
            s_path.popleft()
            t_path.popleft()
        
        return 'U' * len(s_path) + ''.join(t_path)