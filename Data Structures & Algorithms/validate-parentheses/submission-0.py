class Solution:
    def isValid(self, s: str) -> bool:
        stack = ""
        for c in s:
            stack += c
            print(stack[-2:])
            if stack[-2:] == "[]" or stack[-2:] == "()" or stack[-2:] == "{}":
                stack = stack[:-2]
        if not stack:
            return True
        return False