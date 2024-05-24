from random import randint
from tkinter import *
from abc import ABC, abstractmethod

class MatrixDisplay(ABC):
    def __init__(self, matrix, cell_size):
        self.matrix = matrix
        self.cell_size = cell_size

    @abstractmethod
    def show(self):
        pass

class TkMatrixDisplay(MatrixDisplay):
    def __init__(self, root, matrix, cell_size):
        super().__init__(matrix, cell_size)
        self.root = root
        self.canvas = Canvas(root, width=len(matrix[0]) * cell_size, height=len(matrix) * cell_size, borderwidth=0, highlightthickness=0, bg='white')
        self.canvas.pack(expand=True)
        self.center_canvas()
        self.create_buttons()
        self.score_counter = ScoreCounter(root)
        self.show()

    def center_canvas(self):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        canvas_width = len(self.matrix[0]) * self.cell_size
        canvas_height = len(self.matrix) * self.cell_size
        x_center = (screen_width - canvas_width) // 2
        y_center = (screen_height - canvas_height) // 2
        self.canvas.place(x=x_center, y=y_center)

    def create_buttons(self):
        button_frame = Frame(self.root, bg='lightgrey')
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        button_frame.place(x=(screen_width - 150) // 2, y=screen_height - 150)

        btn_up = Button(button_frame, text="↑", command=self.move_up, width=5, height=2)
        btn_up.grid(row=0, column=1, padx=5, pady=5)

        btn_left = Button(button_frame, text="←", command=self.move_left, width=5, height=2)
        btn_left.grid(row=1, column=0, padx=5, pady=5)

        btn_down = Button(button_frame, text="↓", command=self.move_down, width=5, height=2)
        btn_down.grid(row=1, column=1, padx=5, pady=5)

        btn_right = Button(button_frame, text="→", command=self.move_right, width=5, height=2)
        btn_right.grid(row=1, column=2, padx=5, pady=5)

    def show(self):
        for row in range(len(self.matrix)):
            for col in range(len(self.matrix[row])):
                x_up = col * self.cell_size
                y_up = row * self.cell_size
                self.canvas.create_rectangle(x_up, y_up, x_up + self.cell_size, y_up + self.cell_size, fill='white', outline='black')
                if self.matrix[row][col][1] > 0:
                    colors = ['lightgreen', 'blue', 'red', 'yellow', 'purple', 'green']
                    color_index = self.matrix[row][col][1] - 1
                    self.canvas.create_rectangle(x_up, y_up, x_up + self.cell_size, y_up + self.cell_size, fill=colors[color_index], outline='black')

    def move_up(self):
        print("Move up")

    def move_down(self):
        print("Move down")

    def move_left(self):
        print("Move left")

    def move_right(self):
        print("Move right")

    def on_cell_click(self, row, col):
        points = self.matrix[row][col][1]
        self.score_counter.update_score(points)

class ScoreCounter:
    def __init__(self, root):
        self.root = root
        self.score = 0
        self.label = Label(root, text="Score: 0", font=("Arial", 16), bg="lightgrey")
        self.label.place(x=20, y=20)

    def update_score(self, points):
        self.score += points
        self.label.config(text="Score: {}".format(self.score))

def main():
    rr = randint(1, 6)
    cell_size = 30
    matrix = [
        [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
        [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
        [[0, 0], [0, 0], [0, 0], [1, rr], [1, rr], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
        [[0, 0], [0, 0], [0, 0], [0, 0], [1, rr], [1, rr], [0, 0], [0, 0], [0, 0], [0, 0]],
        [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
        [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
        [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
        [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
        [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
        [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
        [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
        [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
        [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
        [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
        [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
        [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
        [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
        [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
        [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
        [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
        [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
        [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
        [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
        [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
    ]

    root = Tk()
    root.title('Matrix Display 10x24')
    root.attributes('-fullscreen', True)
    root.configure(background='lightgrey')

    display = TkMatrixDisplay(root, matrix, cell_size)
    root.mainloop()

if __name__ == "__main__":
    main()
# ghghgh