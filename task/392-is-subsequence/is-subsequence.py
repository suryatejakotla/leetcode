class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        param1=0
        param2=0
        while(param1<len(s) and param2<len(t)):
                if s[param1]==t[param2]:
                    param1+=1
                param2+=1
        return len(s)==param1