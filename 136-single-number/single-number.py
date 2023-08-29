class Solution:
    def singleNumber(self, arr: List[int]) -> int:
        n=len(arr)
        arr.sort()
        n=len(arr)
        if n==1:
            return arr[0]
        for i in range(0,n):
            if i==0:
                if arr[i]==arr[i+1]:
                    continue
                else:
                    return arr[0]
            elif i==n-1:
                if arr[i]==arr[i-1]:
                    continue
                else:
                    return arr[n-1]
            else:
                if arr[i]==arr[i-1] or arr[i]==arr[i+1]:
                    continue
                else:
                    return arr[i]
                