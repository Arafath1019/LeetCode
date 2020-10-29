class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        list1=[] 
        list1[:0]=ransomNote 
        
        list2 = []
        list2[:0] = magazine
        
        temp = True
        
        for i in range(len(list1)):
            if list1[i] in list2:
                a = list2.index(list1[i])
                list2[a] = "removed"
            else:
                temp = False
        return temp