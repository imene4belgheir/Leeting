class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False  

        n = 0
        d = 0
        p = x

        
        while p > 0:
            d += 1
            p //= 10

        p = x  
        for i in range(d):
            n += (p % 10) * (10 ** (d - i - 1))
            p //= 10

        return n == x
