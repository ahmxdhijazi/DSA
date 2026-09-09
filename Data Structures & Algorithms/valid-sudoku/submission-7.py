class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for row in range(9):
            seen = set()
            for i in range(9):
                if board[row][i] == ".":
                    continue
                if board[row][i] in seen:
                    return False
                seen.add(board[row][i])

        for col in range(9):
            seen = set()
            for i in range(9):
                if board[i][col] == ".":
                    continue
                if board[i][col] in seen:
                    return False
                seen.add(board[i][col])

        #Unsure about the math for the squares.
        for square in range(9): #The full square
            seen = set()
            for i in range(3): #row
                for j in range(3): #column
                    row = (square//3) * 3 + i #math returning row?
                    col = (square % 3) * 3 + j #math returning column?
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col]) #Seen set

        return True