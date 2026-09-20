class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key = lambda x: x[1])
        n=len(intervals)

        p=0
        c=1

        for i in range(1,n):
            if intervals[i][0]>=intervals[p][1]:
                c+=1
                p=i
        return n-c
                
