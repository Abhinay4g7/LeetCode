class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first=-1
        last=-1
        low=0
        new=[]
        high=len(nums)-1
        low1=0
        high1=len(nums)-1
        while(low<=high):
            mid=(low+high)//2
            if nums[mid]==target:
                first=mid
                high=mid-1
            elif nums[mid]<target:
                low=mid+1
            else:
                high=mid-1
        new+=[first]
        while(low1<=high1):
            mid=(low1+high1)//2
            if nums[mid]==target:
                last=mid
                low1=mid+1
            elif nums[mid]<target:
                low1=mid+1
            else:
                high1=mid-1
        new+=[last]
        return new





