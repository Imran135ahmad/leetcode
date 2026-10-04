class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1 or numRows>=len(s):
            return s
        row=[""]*numRows
        direction=1
        cR=0
        for ch in s:
            row[cR]+=ch
            if cR==0:
                direction=1
            elif cR==numRows-1:
                direction = -1
            cR+=direction
        return "".join(row)