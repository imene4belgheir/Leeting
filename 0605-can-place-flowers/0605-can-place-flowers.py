class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        p=0
        i=0
        left_empty, right_empty = True, True
        while(p<n and i < len(flowerbed)):
            if flowerbed[i]==0:
                left_empty = (i==0 or flowerbed[i-1] == 0)
                right_empty = (i == len(flowerbed) - 1 or flowerbed[i+1]==0)
                if left_empty and right_empty :
                    flowerbed[i] = 1
                    p += 1
                    i += 1
            i +=1
        return p>=n



