class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for i in range(len(nums)):
            dic[nums[i]] = i 

        for i in range(len(nums)):
            a = target - nums[i]
            b = dic.get(a, -1)
            if b != -1 and b != i:  
                return list((i, b))
        
        return -1  
