class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q=deque()
        ans=[]
        q.append(root)
        while q:
            tmp=deque()
            cur=[]
            while q:
                node=q.popleft()
                cur.append(node.val)
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            ans.append(cur)
            q=tmp
        return ans
        