class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        def bcktrck(pos, cur, total):
            if target == total:
                res.append(cur.copy())
                return
            elif total > target:
                return
        
            prev = -1
            for i in range(pos, len(candidates)):
                if candidates[i] == prev:
                    continue
                cur.append(candidates[i])
                bcktrck(i + 1, cur, total + candidates[i])
                cur.pop()
                prev = candidates[i]
        
        bcktrck(0, [], 0)
        return res
                
                
            