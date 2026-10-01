class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack= []
        pairs = sorted(zip(position, speed), reverse=True)
        times = [(target-p)/s for p, s in pairs]
        for t in times:
            if not stack or t > stack[-1]:
                stack.append(t)
        return len(stack)