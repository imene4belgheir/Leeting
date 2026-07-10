class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        output = ""
        s = s.strip()
        k = 0
        
        for i in range(len(s) - 1, -1, -1):
            
            if s[i] == " ":
         
                space = 1 if k > 0 else 0 
                
                if space == 1:
                    output += s[i+1 : i + 1 + k] + " "
                    k = 0
            else:
                k += 1

                if i == 0:
                    output += s[0 : 0 + k + 1]

        
        return output.strip()