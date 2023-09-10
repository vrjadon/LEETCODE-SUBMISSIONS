class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        a=set(nums1)
        b=set(nums2)
        res1=[]
        res2=[]
        res1=a-b
        res2=b-a
        res=[]
        res.append(res1)
        res.append(res2)
        return res
