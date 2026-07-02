class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        
        max=candies[0]
        for i in range (1, len(candies)):
            if max <= candies[i]:
                max = candies[i]
        
        result = [(candies[i] + extraCandies) >= max for i in range(len(candies))]
        return result