class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        List= []
        n_nums = sorted(nums)
    
        for i in range (len(n_nums)):
            if n_nums[i] == target:
                List.append(i)
        return List
