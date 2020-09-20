class Solution:
    def isHappy(self, n: int) -> bool:

      s = set()

      while n != 1:
            if n in s: 
              return False
            s.add(n)

            result = 0
            while n:
                result = result + (n % 10) ** 2
                n = n // 10
            n = result
      return True
