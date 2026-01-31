class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        """x=123
        output=321"""
        sign = -1 if x < 0 else 1
        x_abs = abs(x)
        reversed_x = int(str(x_abs)[::-1])
        result = sign * reversed_x
        if result < -2**31 or result > 2**31 - 1:
            return 0
        return result
        