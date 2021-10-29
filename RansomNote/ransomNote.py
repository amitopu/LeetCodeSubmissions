class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomDict = {}
        magazineDict = {}
        
        # collect ransomNote char frequency
        for i in ransomNote:
            if ransomDict.get(i, -1) == -1:
                ransomDict[i] = 1
            else:
                ransomDict[i] += 1
        
        # collect magazine chat frequency
        for j in magazine:
            if magazineDict.get(j, -1) == -1:
                magazineDict[j] = 1
            else:
                magazineDict[j] += 1
        
        # check if all char in ransomNote can be covered by magazine
        count = 0
        for elem in ransomDict.keys():
            if magazineDict.get(elem, -1) >= ransomDict[elem]:
                count += 1
        
        if count == len(ransomDict.keys()):
            return True
        else:
            return False



# different solution reduces memory requirement

# class Solution:
#     def canConstruct(self, ransomNote: str, magazine: str) -> bool:
#         magazineDict = {}
        
#         for j in magazine:
#             if magazineDict.get(j, -1) == -1:
#                 magazineDict[j] = 1
#             else:
#                 magazineDict[j] += 1
        
#         count = 0
#         for i in ransomNote:
#             if magazineDict.get(i, -1) > 0:
#                 magazineDict[i] -= 1
#                 count += 1
                
#         if count == len(ransomNote):
#             return True
#         else:
#             return False

# another solution which is better than others

# class Solution:
#     def canConstruct(self, ransomNote: str, magazine: str) -> bool:
#         n = len(ransomNote)
#         m = len(magazine)
        
#         for i in ransomNote:
#             if i not in magazine:
#                 break
#             magazine = magazine.replace(i,'',1)
        
#         return len(magazine) == m - n