class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        opening = set('({[')
        mapping = {")": "(", "}": "{", "]": "["}
        for char in s:
            if char in opening:
                stack.append(char)
            elif stack and mapping[char] == stack[-1]:
                stack.pop()
            else:
                return False
        return not stack