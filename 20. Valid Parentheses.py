class Solution:
    def isValid(self, s: str) -> bool:
        
        temp = []
        
        for char in s:
            if char in ["(", "{", "["]:
                temp.append(char)
            
            else:
                if not temp:
                    return False
                
                current_char = temp.pop()
                
                if current_char == '(': 
                    if char != ")": 
                        return False
                if current_char == '{': 
                    if char != "}": 
                        return False
                if current_char == '[': 
                    if char != "]": 
                        return False
                
        if temp: 
            return False
        return True
        