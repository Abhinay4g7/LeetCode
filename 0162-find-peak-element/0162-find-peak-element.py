class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        elif nums[0]>nums[1]:
            return 0
        elif nums[len(nums)-1]>nums[len(nums)-2]:
            return len(nums)-1
        else:
            for i in range(len(nums)):
                if nums[i-1]<nums[i]>nums[i+1]:
                    return i

        