class Solution:
    def isValid(self, s: str) -> bool:
        dict = {")": "(", "]": "[", "}": "{"}
        stack = []
        for char in s:
            if char in dict:
                if not stack or stack.pop() != dict[char]:
                    return False
            else:
                stack.append(char)
        return not stack
        