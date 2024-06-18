class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.split()
        s.reverse()
        ans=' '.join(s)
        return ans