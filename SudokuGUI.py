from tkinter import Tk, Canvas, Frame, Button, BOTH, TOP, BOTTOM
margin = 20  # margin for the board
side = 50  # side for each box
width = height = margin * 2 + side * 9  # width of the window, 2 margins (left, right) with 9 side


class SudokuSolver:
    def __init__(self, board=[[0 for _ in range(9)] for _ in range(9)]):
        self.board = board

    def reset(self):
        self.board = [[0 for _ in range(9)] for _ in range(9)]

    def show(self):
        for i in range(len(self.board)):
            if i % 3 == 0 and i != 0:
                print("-------------------------")
            for j in range(len(self.board[0])):
                if j % 3 == 0 and j != 0:
                    print(" | ", end="")

                if j == 8:
                    print(self.board[i][j])
                else:
                    print(self.board[i][j], end="")

    def check_valid_board(self):
        def isRowValid(row=[]):
            seen = set()
            for col in range(9):
                if row[col] == 0:
                    continue

                if row[col] in seen:
                    return False

                seen.add(row[col])
            return True

        def isColValid(board, col):
            seen = set()
            for row in range(9):
                if board[row][col] == 0:
                    continue

                if board[row][col] in seen:
                    return False

                seen.add(board[row][col])
            return True

        def isSquareValid(board, row, col):
            seen = set()
            for r in range(row, row + 3):  # 0-2, 3-5, 6-8
                for c in range(col, col + 3):  # 0-2, 3-5, 6-8
                    if board[r][c] == 0:
                        continue
                    if board[r][c] in seen:
                        return False
                    seen.add(board[r][c])
            return True

        for i in range(len(self.board)):
            if not isRowValid(self.board[i]):
                return False

            if not isColValid(self.board, i):
                return False

        for r in range(0, len(self.board), 3):  # 0, 3, 6
            for c in range(0, len(self.board[0]), 3):  # 0, 3, 6
                if not isSquareValid(self.board, r, c):
                    return False

        return True

    def valid_num(self, position, val):
        r, c = position
        # check row
        for i in range(len(self.board[0])):
            if self.board[i][c] == val and i != r:
                return False

        # check col
        for i in range(len(self.board)):
            if self.board[r][i] == val and i != c:
                return False

        # check grid
        box_x = c // 3
        box_y = r // 3

        for i in range(box_y * 3, box_y * 3 + 3):
            for j in range(box_x * 3, box_x * 3 + 3):
                if self.board[i][j] == val and (i, j) != (r, c):
                    return False

        return True

    def find_empty(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if self.board[i][j] == 0:
                    return (i, j)  # return (row, col)
        return False

    def solve(self):
        # Starting Recursion
        find = self.find_empty()
        if not find:  # If everything is already filled
            return True

        row, col = find
        for n in range(1, 10):
            if self.valid_num((row, col), n):
                self.board[row][col] = n
                if self.solve():  # when everything is already filled, return the board
                    return True

                self.board[row][col] = 0

        return False


class SudokuUI(Frame):
    def __init__(self, window, game):
        self.game = game
        self.window = window
        self.row, self.col = -1, -1

        self.__initUI()

    def __initUI(self):
        self.window.title("Sudoku Solver")
        self.canvas = Canvas(width=width, height=height)
        self.canvas.pack(fill=BOTH, side=TOP)
        clear_button = Button(text="Reset Board", command=self.__clear_answers)
        solve_button = Button(text="Solve", command=self.__show_answer)
        clear_button.pack(side=BOTTOM)
        solve_button.pack(side=BOTTOM)

        self.draw_grid()

        self.canvas.bind("<Button-1>", self.__cell_clicked)
        self.canvas.bind("<Key>", self.__key_pressed)

    def __show_answer(self):
        if self.game.check_valid_board():
            self.game.solve()
            self.draw_board()
        else:
            self.draw_impossible()

    def __clear_answers(self):
        self.game.reset()
        self.canvas.delete("impossible")
        self.draw_board()

    def draw_grid(self):
        for i in range(10):
            color = "grey0" if i % 3 == 0 else "gray80"

            # print row
            x0 = margin
            y0 = margin + (i * side)
            x1 = width - margin
            y1 = margin + (i * side)
            self.canvas.create_line(x0, y0, x1, y1, fill=color)
            # print col
            x0 = margin + (i * side)
            y0 = margin
            x1 = margin + (i * side)
            y1 = height - margin
            self.canvas.create_line(x0, y0, x1, y1, fill=color)

    def draw_impossible(self):
        x0 = y0 = margin + side * 2
        x1 = y1 = margin + side * 7
        self.canvas.create_rectangle(
            x0, y0, x1, y1,
            tags="impossible", fill="red", outline="Orange"
        )
        x = y = margin + 4 * side + side / 2
        self.canvas.create_text(
            x, y,
            text="Board Cannot be Solved", tags="impossible",
            fill="white", font=("Arial", 20)
        )

    def __draw_cursor(self):
        self.canvas.delete("cursor")
        if self.row >= 0 and self.col >= 0:
            x0 = margin + self.col * side + 1
            y0 = margin + self.row * side + 1
            x1 = margin + (self.col + 1) * side - 1
            y1 = margin + (self.row + 1) * side - 1
            self.canvas.create_rectangle(
                x0, y0, x1, y1,
                outline="blue", tags="cursor"
            )

    def draw_board(self):
        self.canvas.delete("numbers")
        for i in range(9):
            for j in range(9):
                answer = self.game.board[i][j]
                if answer != 0:
                    x = margin + (j * side) + side // 2  # put it in the middle of the box
                    y = margin + (i * side) + side // 2
                    color = "black"
                    self.canvas.create_text(x, y, text=answer, tags="numbers", fill=color)

    def __cell_clicked(self, event):
        x, y = event.x, event.y
        if margin < x < width - margin and margin < y < height - margin:
            self.canvas.focus_set()

            # get row and col numbers from x,y coordinates
            row, col = (y - margin) // side, (x - margin) // side  # row, col for the selected box

            # if cell was selected already - deselect it
            print(self.game.board)
            if (row, col) == (self.row, self.col):
                self.row, self.col = -1, -1
            elif 0 <= self.game.board[row][col] <= 9:
                self.row, self.col = row, col
        else:  # out of the board
            self.row, self.col = -1, -1

        self.__draw_cursor()

    def __key_pressed(self, event):
        # if cursor is valid and key pressed is valid
        if self.row >= 0 and self.col >= 0 and event.char in "1234567890":
            self.game.board[self.row][self.col] = int(event.char)
            self.col, self.row = -1, -1  # Un-select box
            self.draw_board()
            self.__draw_cursor()


test_board = [
    [0, 0, 0,   0, 0, 0,   0, 0, 0],
    [0, 0, 0,   0, 0, 0,   0, 0, 0],
    [8, 0, 0,   0, 0, 0,   0, 0, 0],

    [4, 0, 0,   0, 0, 0,   0, 0, 0],
    [7, 0, 0,   0, 0, 0,   0, 0, 0],
    [0, 0, 0,   0, 0, 0,   8, 0, 0],

    [0, 1, 0,   0, 0, 5,   0, 0, 0],
    [0, 0, 0,   0, 0, 0,   0, 0, 0],
    [0, 5, 0,   0, 0, 0,   1, 0, 0]
]

game = SudokuSolver()
window = Tk()
SudokuUI(window, game)
window.mainloop()
