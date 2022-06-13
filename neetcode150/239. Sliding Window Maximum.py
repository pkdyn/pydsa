class Solution:
    #n, n
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        #no. of k size windows for size n: n-k+1
        l = r = 0
        res = []
        #ds used: dequue (monotonic decrease)
        #why queue over stack: to add/rem elements from both sides
        dq = collections.deque() #hold indices
        
        while r < len(nums):
            #pop smaller value
            while dq and nums[dq[-1]] < nums[r]:
                dq.pop()
            #push larger value
            dq.append(r)
            
            #czk window size before appending highest value
            if (r - l + 1) == k:
                res.append(nums[dq[0]])
                #update left pointer to slide window
                l += 1
                
            #pop from left to slide window
            if l > dq[0]:
                dq.popleft()
                
            r += 1
        return res
                