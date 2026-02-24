class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) <= 1: 
            return nums
        mid = len(nums) 
        left = self.sortArray(nums[:mid]) 
        right = self.sortArray(nums[mid:]) 
        return self.merge(left, right)

    def merge(self, left, right):
        i = 0 
        j = 0 
        result = []
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i]) 
                i += 1
            else:
                result.append(right[j])  
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result