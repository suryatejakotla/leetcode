class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x<0:
            return False
        s=x
        res=0
        while(x>0):
            k=x%10
            res=res*10+k
            x//=10
        return res==s