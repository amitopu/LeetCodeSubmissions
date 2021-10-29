class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n = len(s)
        m = len(t)
        
        if n == m:
            for i in s:
                t = t.replace(i,'',1)
        else:
            return False
        
        return len(t) == 0


# Another better solution

# class Solution:
#      def isAnagram(self, s: str, t: str) -> bool:
            
#         #return set(Counter(s).items()) == set(Counter(t).items())
#         n = len(s)
#         m = len(t)
        
#         if n == m:
#             return set(Counter(s).items()) == set(Counter(t).items())
#         else:
#             return False