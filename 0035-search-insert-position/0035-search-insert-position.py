class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low=0
        high=len(nums)-1
        temp=nums[high]
        ans=0
        while(low<=high):
            mid=(low+high)//2
            if nums[mid]>=target:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        if target>temp:
            ans=len(nums)
        return ans




        