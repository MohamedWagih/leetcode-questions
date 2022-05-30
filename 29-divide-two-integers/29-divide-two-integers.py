class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == divisor:
            return 1
        
        # if both are the same sign
        positive = (divisor>0 and dividend>0) or (dividend<0 and divisor<0)
        
        divisor = abs(divisor)
        dividend = abs(dividend)
        quotient = 0
        
        while dividend >= divisor:
            shift = 0
            while dividend > divisor<<(shift+1):
                shift += 1
                
            quotient += 1<<shift
            dividend -= divisor<<shift
        
        if not positive:
            quotient = -quotient
    
        return min(max(-2147483648, quotient), 2147483647)