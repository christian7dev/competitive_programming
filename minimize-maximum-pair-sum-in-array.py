class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nlist = []
        list = sorted(nums)
        num = len(list)/2
        for i in range (int(num)):
            sum = list[i] + list[((len(list)-1) - i)]
            nlist.append(sum)
        new_list = sorted(nlist)
        return new_list[-1]
