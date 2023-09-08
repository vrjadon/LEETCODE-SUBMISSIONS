class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp=sorted(nums)
        i=0
        li=[]
        j=len(temp)-1
        while i<j:
            if temp[i]+temp[j]>target:
                j-=1
            elif temp[i]+temp[j]<target:
                i+=1
            else:
                if temp[i]==temp[j]:
                    li.append(nums.index(temp[i]))
                    li.append(nums.index(temp[j],nums.index(temp[i])+1))
                else:
                    li.append(nums.index(temp[i]))
                    li.append(nums.index(temp[j]))

                
                return li


        