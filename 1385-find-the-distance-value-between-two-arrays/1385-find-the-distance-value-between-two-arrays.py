class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        c=0
        for i in range(len(arr1)):
            f=1
            for j in range(len(arr2)):
                if abs(arr1[i]-arr2[j])<=d:
                    f=0
                    break
            if f:
                c+=1
        return c