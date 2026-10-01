class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        tem_stack, idx_stack = [], []
        res = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            while tem_stack and t > tem_stack[-1]:
                tem_stack.pop()
                idx = idx_stack.pop()
                res[idx] = i - idx
            tem_stack.append(t)
            idx_stack.append(i)
        return res