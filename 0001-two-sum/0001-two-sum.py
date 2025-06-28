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

# Usage
nums = [2, 7, 11, 15]
target = 9
solution = Solution()
output = solution.twoSum(nums, target)
print(output)  # Output: [0, 1]
