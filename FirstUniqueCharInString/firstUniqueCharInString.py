class Solution:
    def firstUniqChar(self, s: str) -> int:
        myDict = {}
        n = len(s)
        
        # iterate over the string and store char frequency in myDict
        for i in s:
            if myDict.get(i, -1) == -1:
                myDict[i] = 1
            else:
                myDict[i] += 1
        
        # iterate over the string and 
        # if a char only exists sigle time return the index of first occurance
        for j in range(n):
            if myDict[s[j]] == 1:
                return j
            
        return -1

        