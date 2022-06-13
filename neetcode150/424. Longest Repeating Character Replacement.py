class Solution:
    #n, n
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        res = 0
        chCnt = {} # to tally character count
        for r in range(len(s)):
            chCnt[s[r]] = 1 + chCnt.get(s[r], 0)
            #size of window - maxChCnt <= k -> k ops sufficient to make window homo
            while (r - l + 1) - max(chCnt.values()) > k: #window cant be made homo
                #shift left pntr to slide window
                chCnt[s[l]] = -1 + chCnt.get(s[l], 0)
                l += 1
            #longest possible homo window
            res = max(res, r - l + 1)
        return res
            