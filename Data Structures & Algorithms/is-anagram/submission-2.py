class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Coutner(t)
        