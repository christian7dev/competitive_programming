class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        list = []
        for i in nums:
            list.append(int(i))
        num_sort = sorted(list , reverse = True)
        return str(num_sort[k-1])
