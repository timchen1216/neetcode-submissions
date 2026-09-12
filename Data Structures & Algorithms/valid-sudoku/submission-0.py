class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def isDuplicate(self, nums: List[str]) -> bool:
            count = {}
            for s in nums:
                count[s] = count.get(s, 0) +1
            for k, v in count.items():
                if k != "." and v > 1:
                    return True
            return False

        for i in range(9):
            row = board[i]
            col = [board[r][i] for r in range(9)]
            box = [board[(i//3)*3 + r][(i%3)*3 + c] for r in range(3) for c in range(3)]
            if isDuplicate(self,row) or isDuplicate(self,col) or isDuplicate(self,box):
                return False               
        return True