class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        low=0
        high=len(nums)-1
        ans=0
        if len(nums)==1:
            ans=0
        elif nums[0]>nums[1]:
            ans=0
        elif nums[high]>nums[high-1]:
            return high
        else:
            while(low<=high):
                mid=(low+high)//2
                if mid==0:
                    if nums[mid]>nums[mid+1]:
                        ans=mid
                    else:
                        ans=mid+1
                if nums[mid-1]<nums[mid]>nums[mid+1]:
                    ans=mid
                    break
                elif nums[mid]>nums[mid-1]:
                    low=mid+1
                else:
                    high=mid-1
        return ans
