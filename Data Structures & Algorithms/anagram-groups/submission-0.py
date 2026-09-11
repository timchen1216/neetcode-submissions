class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupMap = {}
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            key = tuple(count)
            groupMap.setdefault(key, []).append(s)
        return list(groupMap.values())