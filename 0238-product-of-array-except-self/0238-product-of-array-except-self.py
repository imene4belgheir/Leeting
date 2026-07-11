class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        prefixes = [1] * len(nums)
        suffixes = [1] * len(nums)

        for i in range(1, len(prefixes)):
            prefixes[i] = prefixes[i - 1] * nums[i - 1]

        for i in range(len(suffixes) - 2, -1, -1):
            suffixes[i] = suffixes[i+1] * nums[i + 1]

        output = [1] * len(nums)

        for i in range (len(nums)):
            output[i] = suffixes[i] * prefixes[i]
    
        return output
    
