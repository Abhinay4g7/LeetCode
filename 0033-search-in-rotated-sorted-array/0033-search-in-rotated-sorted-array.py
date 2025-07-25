class Solution:
    def search(self, nums: List[int], target: int) -> int:
        ans=-1
        low=0
        high=len(nums)-1
        while(low<=high):
            mid=(low+high)//2
            if nums[mid]==target:
                ans=mid
                break
            else:
                if (nums[mid]==nums[low]) and (nums[mid]==nums[high]):
                    low+=1
                    high-=1
                elif (nums[low]<=nums[mid]):
                    if (target>=nums[low] and target<=nums[mid]):
                        high=mid-1
                    else:
                        low=mid+1
                    
                else:
                    if target>=nums[mid] and target<=nums[high]:
                        low=mid+1
                    else:
                        high=mid-1
        return(ans)