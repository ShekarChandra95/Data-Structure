class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x <0:
            return False

        a = str(x)
        return a == a[::-1]
        # Org = x
        # rev_num = 0
        # while x >0:
        #     digit = x % 10
        #     rev_num = rev_num * 10 + digit
        #     x // 10
        #     return Org == rev_num
    
        
        