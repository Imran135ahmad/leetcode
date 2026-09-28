class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.split()
        ans=[]

        for w in s:
            ans.append(w[::-1])
        return " ".join(ans)