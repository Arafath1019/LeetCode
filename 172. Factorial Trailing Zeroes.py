class Solution:
    def trailingZeroes(self, n: int) -> int:
        
        i = 5
        no_of_zeros = 0
        
        while n >= i:
            no_of_zeros += n // i
            i *= 5
        
        return no_of_zeros