class Solution:
    #n*4^n, n
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        d2cdict = {
            "2" : "abc",
            "3": "def",
            "4": "ghi", 
            "5": "jkl", 
            "6": "mno", 
            "7": "pqrs", 
            "8": "tuv", 
            "9": "wxyz"      
        }
        
        def bcktrck(i, cur):
            if len(cur) == len(digits):
                res.append(cur)
                return
            for c in d2cdict[digits[i]]:
                bcktrck(i + 1, cur + c)
        if digits: #making suure not empty
            bcktrck(0, "")
        return res