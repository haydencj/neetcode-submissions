class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # go square by square. 
        # if square is '.'? continue
        # else? check if in our sets. 
        # in our sets? return false 
        # not? add to col, row, and box sets

        # key will be # of row, col, box
        # value will be seen numbers
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for r in range(9): # rows
            for c in range(9): # cols
                current_val = board[r][c]
                current_box = (r // 3, c // 3) # tuple is hashable (bc immutable), so can be used as key

                if current_val == ".": continue

                if (current_val in rows[r]
                    or current_val in cols[c]
                    or current_val in boxes[current_box]):
                        return False
                
                # still valid, add to sets
                rows[r].add(current_val)
                cols[c].add(current_val)
                boxes[current_box].add(current_val)
            
        return True

