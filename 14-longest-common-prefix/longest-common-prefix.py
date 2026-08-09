class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        strs.sort()
        S = ""
        x = 0
        l = len(strs)

        while x < len(strs[0]):
            if strs[0][x] == strs[l-1][x]:
                S += strs[0][x]
            else:
                break
            x += 1
        return S