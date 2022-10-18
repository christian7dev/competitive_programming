import math
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if( n > 0):
            if math.log(n,4) == int(math.log(n,4)):
                return True
