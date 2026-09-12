class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        if not s:
            return [""]
        R=self.letterCasePermutation(s[1:])
        if s[0].isalpha():
            return [s[0].lower() + x for x in R] + [s[0].upper() + x for x in R]
        else:
            return [s[0]+x for x in R]
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  