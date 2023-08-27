class Solution:
    def rotate(self, nums, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        k=k%n
        if n<=1 or k==0:
            return nums
        temp=nums[-k:]
        nums[k:]=nums[:n-k]
        nums[:k]=temp
        return nums