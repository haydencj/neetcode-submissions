class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for r in range(9):
            for c in range(9):
                current_val = board[r][c]
                current_box = (r // 3, c // 3)

                if current_val == ".":
                    continue
                
                if (current_val in rows[r]
                    or current_val in cols[c]
                    or current_val in boxes[current_box]):
                    
                    return False

                rows[r].add(current_val)
                cols[c].add(current_val)
                boxes[current_box].add(current_val)

        return True