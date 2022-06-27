class Solution:
    #log(n + m), n + m
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        A, B = nums1, nums2
        if len(A) > len(B):
            A, B = B, A #making sure A is smaller
        total = len(A) + len(B)
        l, r = 0, len(A) - 1
        while True:
            m = (l + r) // 2
            n = (total // 2) - (m + 1) - 1 #index + 1 = no. of elements
            
            #infinity to take care of edge cases: default smallest val and default largest val
            Al = A[m] if m >= 0 else float("-infinity") #
            Ar = A[m + 1] if m + 1 < len(A) else float("infinity") 
            Bl = B[n] if n >= 0 else float("-infinity")
            Br = B[n + 1] if n + 1 < len(B) else float("infinity")
            
            if Al <= Br and Bl <= Ar: #properly sorted 
                if total % 2: #1 => odd
                    return min(Ar, Br)
                else: #0 => even
                    return (max(Al, Bl) + min(Ar, Br)) / 2 #avg of mid vals
            elif Al > Br:
                r = m - 1 #search in left region
            elif Bl > Ar:
                l = m + 1 #search in right region
        return
        