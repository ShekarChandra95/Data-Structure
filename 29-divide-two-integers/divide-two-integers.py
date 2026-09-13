class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        max_int = 2**31 - 1
        min_int = -2**31

        # Handle overflow case
        if dividend == min_int and divisor == -1:
            return max_int
            
        # determine the sign result
        negative = (dividend<0) != (divisor <0)
        
        # work with absolute values
        dividend, divisor = abs(dividend), abs(divisor)
        quotient = 0
        while dividend >= divisor:
            temp, multiple = divisor, 1

            # double the divisor until it's bigger than dividend
            while dividend >=(temp<<1):
                temp<<=1
                multiple <<=1
            dividend -= temp
            quotient += multiple

        result = -quotient if negative else quotient
        return max(min_int, min(max_int, result))
