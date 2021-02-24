# kyle Goldrick
# kcg2rr
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        result = 0
        if x < 0:
            return -self.reverse(-x)

        while x:
            result = result * 10 + x % 10
            x =  x/10
        
        if result <= 2147483647:
            return result
        else:
            return 0