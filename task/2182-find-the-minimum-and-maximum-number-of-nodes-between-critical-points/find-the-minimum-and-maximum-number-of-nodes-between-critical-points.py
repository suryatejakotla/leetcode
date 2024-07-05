# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
	    ans = [float('inf'), -float('inf')]
	    curr = head.next
	    prev = head
	    i = 1
	    pos = []
	    while(curr.next):
		    if(prev.val < curr.val > curr.next.val):
			    pos.append(i)
		    elif(prev.val > curr.val < curr.next.val):
			    pos.append(i)
		    i += 1
		    prev, curr = curr, curr.next
	    if(len(pos) < 2):
		    return -1, -1
	    for i in range(1, len(pos)):
		    ans[0] = min(ans[0], pos[i]-pos[i-1])
	    ans[1] = pos[-1]-pos[0]
	    return ans
	