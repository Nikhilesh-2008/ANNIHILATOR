class Solution:
    def maxCoins(self, piles: list[int]) -> int:
        piles.sort()
        my=0
        n=len(piles)//3
        for i in range(len(piles)-2,-1,-2):
            if n>0:
                my+=piles[i]
                n-=1
            else:
                break
        return my