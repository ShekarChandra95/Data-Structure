class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        order = {')':'(', ']':'[', '}':'{'}
        stack = []
        for char in s:
            if char in order.values():
                stack.append(char)
            elif char in order:
                if not stack or order[char] != stack.pop():
                    return False
        return not stack       