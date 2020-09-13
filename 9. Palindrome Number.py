class Solution:
    def isPalindrome(self, x: int):
        reverse = 0
        if x == 0:
          return True

        elif x > 0:
          num = x
          while x != 0:
              remainder = x % 10
              reverse = reverse * 10 + remainder
              x = int(x / 10)
          if num == reverse:
            return True
        else: 
          return False