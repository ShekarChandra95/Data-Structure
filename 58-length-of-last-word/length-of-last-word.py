class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        L_word = s.strip().split()

        if not L_word:
            return 0

        return len(L_word[-1])           