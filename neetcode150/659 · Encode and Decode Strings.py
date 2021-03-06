class Solution:
    #n (no. of total characters), n
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        # write your code here
        res = ""
        for s in strs:
            #len + ~ + actual string
            res += str(len(s)) + "~" + s #adding ~ as demiliter
        return res

    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """
    def decode(self, str):
        # write your code here
        res = [] 
        i = 0
        while i < len(str):
            j = i
            while str[j] != "~":
                j += 1
            res.append(str[j + 1: j + 1 + int(str[i:j])]) #int(str[i:J]) converts the length int -> str
            i= j + 1 + int(str[i:j])

        return res



