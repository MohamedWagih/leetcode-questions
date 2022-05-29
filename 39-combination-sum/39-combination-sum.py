class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        combinations = []
        
        def dfs(i, curr_combination, curr_combination_sum):
            if i >= n or curr_combination_sum > target:
                return
            if curr_combination_sum == target:
                combinations.append(curr_combination.copy())
                return
            
            # make to branches 
            
            # 1) append current index
            curr_combination.append(candidates[i])
            dfs(i, curr_combination, curr_combination_sum + candidates[i])
            
            # 2) skip currend index
            curr_combination.pop()
            dfs(i+1, curr_combination, curr_combination_sum)
            
        
        dfs(0, [], 0)
        return combinations