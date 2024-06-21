class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ran_cou=Counter(ransomNote)
        mag_cou=Counter(magazine)
        return ran_cou==ran_cou&mag_cou