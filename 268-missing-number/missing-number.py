class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        xor1=0
        xor2=0
        for i in range(n+1):
            xor1^=i
        for ele in nums:
            xor2^=ele
        missing_num=xor1^xor2
        return missing_num