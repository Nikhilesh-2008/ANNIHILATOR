class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        d=[31,28,31,30,31,30,31,31,30,31,30,31]
        def con(date):
            m=int(date[0:2])
            da=int(date[3:5])
            tot=da
            for i in range(m-1):
                tot+=d[i]
            return tot
        a1=con(arriveAlice)
        a2=con(leaveAlice)
        b1=con(arriveBob)
        b2=con(leaveBob)
        s=max(a1,b1)
        e=min(a2,b2)
        if s>e:
            return 0
        return e-s+1