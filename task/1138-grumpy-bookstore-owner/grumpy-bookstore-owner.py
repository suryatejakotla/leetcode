class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
	    m = s = tmp = 0
	    for i in range(len(customers)):
		    if not grumpy[i]: 
			    s += customers[i]                # sum of satisfied customers
			    customers[i] = 0 
		    else: tmp += customers[i]            # sum of grumpy customers 
		    if i>=X: tmp -= customers[i-X]       # remove the leftmost element to keep the sliding window with # of X
		    m = max(m, tmp)                      # max # of satisfied grumpy customers with a secret technique
	    return s+m