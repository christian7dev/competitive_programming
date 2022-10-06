class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        list = []
        count = 0
        for i in nums:
            for x in nums:
                if(i >  x):
                  count += 1
            list.append(count)
            count = 0
        return list  
