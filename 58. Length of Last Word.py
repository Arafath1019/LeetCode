class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        arrayOfWords = s.split(" ")
        if len(arrayOfWords) == 0:
            return 0
        
        lastWord = arrayOfWords[-1]
        return len(lastWord)
