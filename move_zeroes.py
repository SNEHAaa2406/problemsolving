class Solution(object):
    def moveZeroes(self, nums):
        result = []

        for num in nums:
            if num != 0:
                result.append(num)

        for i in range(nums.count(0)):
            result.append(0)

        nums[:] = result
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        