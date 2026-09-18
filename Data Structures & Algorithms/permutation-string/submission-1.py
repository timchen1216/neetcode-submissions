class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n, m = len(s1), len(s2)
        if n > m:
            return False

        count1, count2 = [0] * 26, [0] * 26
        for c in s1:
            count1[ord(c) - ord('a')] += 1
        for i in range(n):
            count2[ord(s2[i]) - ord('a')] += 1

        if count1 == count2:
            return True

        for r in range(n, m):
            count2[ord(s2[r]) - ord('a')] += 1
            count2[ord(s2[r - n]) - ord('a')] -= 1
            if count1 == count2:
                return True
        return False