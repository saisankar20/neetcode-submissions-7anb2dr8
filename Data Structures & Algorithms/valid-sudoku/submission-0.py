class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            seen = set()
            for cell in row:
                if cell != '.':
                    if cell in seen:
                        return False
                    seen.add(cell)

        for c in range(9):
            seen = set()
            for r in range(9):
                cell = board[r][c]
                if cell != '.':
                    if cell in seen:
                        return False
                    seen.add(cell)

        boxes = defaultdict(set)
        for r in range(9):
            for c in range(9):
                cell = board[r][c]
                if cell == '.':
                    continue
                box_key = (r // 3, c // 3)

                if cell in boxes[box_key]:
                    return False
                
                boxes[box_key].add(cell)

        return True