class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        li=[]
        n=len(nums)
        for i in range(n-1):
            for j in range(i+1,n):
                if nums[i]+nums[j]==target:
                    li.append(i)
                    li.append(j)
                    return li

                    
                
        