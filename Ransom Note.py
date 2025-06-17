class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = [0] * 26
        for x in magazine:
            count[ord(x) - ord("a")] += 1
        for x in ransomNote:
            if count[ord(x) - ord("a")] == 0:
                return False
            else:
                count[ord(x)- ord("a")] -=1
        return True