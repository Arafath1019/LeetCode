class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        size = len(strs)
        
        if size == 0:
            return ""
        
        if size == 1:
            return strs[0]
        
        strs.sort()
        
        min_length = min(strs[0], strs[size-1])
        
        min_length = len(min_length)
        
        i = 0
        
        while (i<min_length) and strs[0][i] == strs[size-1][i]:
            i = i+1
        
        if i == 0:
            return ""
        else:
            longest_prefix = strs[0][:i]
            return longest_prefix
        