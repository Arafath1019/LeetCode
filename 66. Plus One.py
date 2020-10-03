class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if len(digits)==1 and digits[0] == 0:
            return [1]
        temp = 0
        digits.reverse()
        for i in range(len(digits)):
            temp += (digits[i] * 10**i)
        temp += 1
        temp = str(temp)
        lst1 = []
        for i in range(len(temp)):
            lst1.append(int(temp[i]))
        
        return lst1
        