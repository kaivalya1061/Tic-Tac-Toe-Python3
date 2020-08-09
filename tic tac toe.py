from tkinter import *
from tkinter import font, messagebox


class TicTacToe:
    def __init__(self, canvas):
        self.canvas = canvas
        self.player = 0
        self.width = 70
        self.dmn = 3
        self.grid = [[-1] * self.dmn for x in range(self.dmn)]
        self.text_font = font.Font(family='Helvetica', size=15, weight='bold')
        self.canvas.bind("<Button-1>", self.click)

    def player_text(self):
        if self.player & 1 == 0:
            self.player = 1
            return "X"
        else:
            self.player = 0
            return "O"

    def winner(self, markers):
        marker_set = set(markers)
        if len(marker_set) == 1 and marker_set.pop() != -1:
            return True
        else:
            return False

    def decide_winner(self, row, column):
        diagonal_match, row_match, col_match = False, False, False
        if row == column:
            diagonal_match = self.winner([self.grid[i][i] for i in range(self.dmn)])
        else:
            row_match = self.winner(self.grid[row])
            col_match = self.winner([self.grid[r][column] for r in range(self.dmn)])
        if diagonal_match or row_match or col_match:
            # print("Winner : Player", self.grid[row][column] + 1)
            return True
        return False

    def click(self, event):
        row = int(event.x / self.width)
        column = int(event.y / self.width)
        if self.grid[row][column] != -1:
            messagebox.showwarning("Warning", "Already Marked")
            return
        coord = lambda x: (x * self.width) + int(self.width / 2)
        self.grid[row][column] = self.player
        self.canvas.create_text(coord(row), coord(column), anchor=CENTER, text=self.player_text(),
                                font=self.text_font)
        won = self.decide_winner(row, column)
        if won:
            messagebox.showinfo("Winner", "Tic Tac Toe Winner : Player" + str(self.grid[row][column] + 1))

    def draw(self):
        x, y, = 0, 0
        for row in self.grid:
            for _ in row:
                self.canvas.create_rectangle(x, y, x + self.width, y + self.width)
                x = x + self.width
            y = y + self.width
            x = 0


master = Tk().title("Tic Tac Toe")
canvas = Canvas(master, width=225, height=225)
canvas.pack()

tic_tac_toe = TicTacToe(canvas)
tic_tac_toe.draw()

mainloop()
