class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for r in range(9): # look at every row
            for c in range(9): # look at every column
                currentNum = board[r][c]
                currentBox = (r // 3, c // 3)
            
                if currentNum == '.':
                    continue 

                # if we've seen this num in this row, col, or box
                if (currentNum in rows[r]
                    or currentNum in cols[c]
                    or currentNum in boxes[currentBox]):
                    print(rows, cols, boxes)
                    return False

                rows[r].add(currentNum)
                cols[c].add(currentNum)
                boxes[currentBox].add(currentNum)

        return True
                    