class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        rom_char = {
            'I': 1 , 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        curr = 0
        tot=0
        prev = 0
        for char in reversed(s):
            curr = rom_char[char]
            if(curr>=prev):
                tot += curr
                prev = curr
            else:
                tot -= curr
        
        return tot