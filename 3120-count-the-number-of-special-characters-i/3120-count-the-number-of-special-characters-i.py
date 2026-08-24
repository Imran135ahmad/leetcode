class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        s=set(word)
        c=0
        for i in range(26):
            l=chr(ord('a')+i)
            u=chr(ord('A')+i)

            if l in s and u in s:
                c+=1
        return c
        