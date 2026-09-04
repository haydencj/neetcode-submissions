class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # go square by square
        # if square is empty? go next
        # not empty? 
        # check if this number has been seen for r, c, box
        # yes? return false
        # no? add number to seen for row, col, box
        # made it to the end? return true
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)
        for r in range(9):
            for c in range(9):
                currentVal = board[r][c]
                box = (r // 3, c // 3) # r = 3, c = 5, box = (1, 1)

                if currentVal == ".": continue
                # check if seen. if seen invalid
                if (currentVal in rows[r] or
                    currentVal in cols[c] or
                    currentVal in boxes[box]):
                    return False
                # not seen? add to seen
                rows[r].add(currentVal)
                cols[c].add(currentVal)
                boxes[box].add(currentVal)
        
        return True
                