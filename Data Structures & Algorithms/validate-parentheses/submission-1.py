class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {")":"(", "]":"[", "}":"{"}
        for char in s:
            if char in stack:
                if not stack or stack.pop() != pairs[char]:
                    return False
            else:
                stack.append(char)
        return True