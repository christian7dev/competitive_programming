class Solution:
    def sortColors(self, nums: List[int]) -> None:
        List = []
        zeros = nums.count(0)
        one = nums.count(1)
        two = nums.count(2)

        for i in range (zeros):
            List.append(0)
        for i in range (one):
            List.append(1)
        for i in range (two):
            List.append(2)
        nums[:] = List
        """
        Do not return anything, modify nums in-place instead.
        """
