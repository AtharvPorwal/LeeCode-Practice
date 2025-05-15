class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        R1 , M1 = Counter(ransomNote) , Counter(magazine)
        if R1 & M1 == R1:
            return True
        return False