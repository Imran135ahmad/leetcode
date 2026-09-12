class Solution:
    def validStrings(self, n: int) -> List[str]:
        ans=[]
        def solve(s,p):
            if len(s)==n:
                ans.append(s)
                return 
            solve(s+"1",1)
            if p!=0:
                solve(s+"0",0)
        solve("",1)
        return ans