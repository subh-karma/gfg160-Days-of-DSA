class Solution:
    def solveSudoku(self, mat):
        # Precompute sets for fast lookup
        self.rows = [set() for _ in range(9)]
        self.cols = [set() for _ in range(9)]
        self.boxes = [set() for _ in range(9)]
        self.board = mat
        self.empty_cells = []

        # Initialize the sets and collect empty cell positions
        for i in range(9):
            for j in range(9):
                num = mat[i][j]
                if num != 0:
                    self.rows[i].add(num)
                    self.cols[j].add(num)
                    self.boxes[self._getBoxIndex(i, j)].add(num)
                else:
                    self.empty_cells.append((i, j))

        self._backtrack(0)

    def _getBoxIndex(self, row, col):
        return (row // 3) * 3 + (col // 3)

    def _backtrack(self, idx):
        if idx == len(self.empty_cells):
            return True  # Solved

        row, col = self.empty_cells[idx]
        box_idx = self._getBoxIndex(row, col)

        for num in range(1, 10):
            if num not in self.rows[row] and num not in self.cols[col] and num not in self.boxes[box_idx]:
                # Place number
                self.board[row][col] = num
                self.rows[row].add(num)
                self.cols[col].add(num)
                self.boxes[box_idx].add(num)

                if self._backtrack(idx + 1):
                    return True

                # Undo the move
                self.board[row][col] = 0
                self.rows[row].remove(num)
                self.cols[col].remove(num)
                self.boxes[box_idx].remove(num)

        return False

