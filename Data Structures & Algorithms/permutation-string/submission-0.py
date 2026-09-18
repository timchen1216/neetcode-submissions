class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        count1, count2 = [0]*26, [0]*26
        l, r = 0, len(s1)-1
        for c in s1:
            count1[ord(c)-ord("a")] += 1
        for i in range(0,len(s1)):
            count2[ord(s2[i])-ord("a")] += 1
            if count1 == count2:
                return True
        l += 1
        r += 1
        while r < len(s2):
            count2[ord(s2[l-1])-ord("a")] -= 1
            count2[ord(s2[r])-ord("a")] += 1

            if count1 == count2:
                return True
            l += 1
            r += 1            
        return False

            