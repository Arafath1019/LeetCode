import math

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if divisor == 0:
            return None
        
        if dividend == 0:
            return 0
        
        if dividend < 0 and divisor > 0:
            result = abs(dividend)/divisor
            result = math.floor(result)
            if result > 2147483648:
                return -2147483648
            return (-1)*result
        
        elif dividend > 0 and divisor < 0:
            result = dividend/abs(divisor)
            result = math.floor(result)
            if result > 2147483648:
                return -2147483648
            return (-1)*result
        
        elif dividend < 0 and divisor < 0:
            result = abs(dividend)/abs(divisor)
            result = math.floor(result)
            if result >= 2147483648:
                return 2147483647
            return result
        
        else:
            result = dividend/divisor
            result = math.floor(result)
            if result >= 2147483648:
                return 2147483647
            return result