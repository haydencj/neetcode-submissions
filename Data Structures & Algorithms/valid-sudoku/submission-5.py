class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # use a hashset to keep track of numbers seen in each row, col, box
        # when a number is seen, add it to row, col, and box

        # to find what box we're in we use integer division.
        # for example if we're in row 6, col 5. 
        # row: 6 // 3 = 2, col: 5 // 3 = 1.
        # we are in box [2, 1]

        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for r in range(9):
            for c in range(9):
                current_val = board[r][c]
                current_box = (r // 3, c // 3) # tuple is hashable - can be used as key

                if current_val == ".":
                    continue
                
                if (current_val in rows[r] or
                    current_val in cols[c] or
                    current_val in boxes[current_box]):
                    return False
                
                rows[r].add(current_val)
                cols[c].add(current_val)
                boxes[current_box].add(current_val)
        
        return True

