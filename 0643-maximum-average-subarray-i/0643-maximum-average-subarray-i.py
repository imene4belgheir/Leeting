class Solution(object):
    def findMaxAverage(self, nums, k):

        n = len(nums)
        if(n<k):
            return
        
        current_sum = sum(nums[:k])
        max_sum = current_sum 

        for i in range(k, n):
            current_sum = current_sum - nums[i-k] + nums[i]
            if current_sum > max_sum :
                max_sum = current_sum
        return float(max_sum)/k
        