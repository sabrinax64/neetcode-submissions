class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {"(":")","{":"}","[":"]"}
        stack = [] #opener

        for char in s:
            if char in pairs:
                stack.append(pairs[char])
            else:                                    # closer
                if not stack or char != stack[-1]:
                    return False
                stack.pop()
               
        return not stack