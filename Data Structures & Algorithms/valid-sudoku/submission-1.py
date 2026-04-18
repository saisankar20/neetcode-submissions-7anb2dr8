class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)
    
        for r in range(9):
            for c in range(9):
                cell = board[r][c]
                if cell == '.':
                    continue
                    
                    # Check row
                if cell in rows[r]:
                    return False
                rows[r].add(cell)
                    
                    # Check column
                if cell in cols[c]:
                    return False
                cols[c].add(cell)
                    
                    # Check box
                box_key = (r // 3, c // 3)
                if cell in boxes[box_key]:
                    return False
                boxes[box_key].add(cell)
            
        return True