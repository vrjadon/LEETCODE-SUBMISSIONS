class Solution:
    def rotate(self, nums, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        k=k%n
        if n<=1:
            return nums
        temp=[]
        for i in range(k):
            temp.append(nums[n - k + i])
        for i in range(n-k-1,-1,-1):
            nums[i+k]=nums[i]

        for i in range(k):
            nums[i]=temp[i]