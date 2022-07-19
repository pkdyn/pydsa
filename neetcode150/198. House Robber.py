class Solution:
    #n, 1
    #rob = max(arr[0] + rob[2:n], rob[1:n])
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        #[rob1, rob2, n, n + 1, ...]
        for n in nums:
            rob1, rob2 = rob2, max(n + rob1,  rob2)
        return rob2