from tkinter import *
from Matrics import Matrics

class TkMatrixDisplay:
    def __init__(self, root, matrix, cell_size):
        self.matrics = matrix
        self.cell_size = cell_size
        self.root = root
        self.canvas = Canvas(root, width=len(self.matrics.matrics[0]) * cell_size, height=len(self.matrics.matrics) * cell_size, borderwidth=0, highlightthickness=0, bg='white')
        self.canvas.pack(expand=True)
        self.center_canvas()
        self.score_counter = ScoreCounter(root)
        self.show()

    def center_canvas(self):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        canvas_width = len(self.matrics.matrics[0]) * self.cell_size
        canvas_height = len(self.matrics.matrics) * self.cell_size
        x_center = (screen_width - canvas_width) // 2
        y_center = (screen_height - canvas_height) // 2
        self.canvas.place(x=x_center, y=y_center)

    def show(self):
        self.canvas.delete("all")  # Clear the canvas before drawing
        for row in range(len(self.matrics.matrics)):
            for col in range(len(self.matrics.matrics[row])):
                x_up = col * self.cell_size
                y_up = row * self.cell_size
                cell_value = self.matrics.matrics[row][col][0]
                if cell_value != 0:
                    r, g, b = [int(val * 255) for val in cell_value]
                    fill_color = f'#{r:02x}{g:02x}{b:02x}'
                else:
                    fill_color = 'white'
                self.canvas.create_rectangle(x_up, y_up, x_up + self.cell_size, y_up + self.cell_size, fill=fill_color, outline='black')

    def iffullrow(self):
        if self.matrics.iffullrow():
            self.show()
            self.iffullrow()
            self.score_counter.update_score(10)
            if self.matrics.matrics[4] == [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0]]:
                self.matrics.end = False

    def move_up(self, event=None):
        self.matrics.centralpovorot()
        self.show()

    def move_down(self, event=None):
        self.matrics.figurefall()
        self.show()

    def move_left(self, event=None):
        self.matrics.left()
        self.show()

    def move_right(self, event=None):
        self.matrics.right()
        self.show()

    def restart_game(self, event=None):
        self.matrics = Matrics()
        self.score_counter.reset_score()
        self.show()

    def close_game(self, event=None):
        self.root.destroy()

class ScoreCounter:
    def __init__(self, root):
        self.root = root
        self.score = 0
        self.max_score = 0
        self.label = Label(root, text=f"Score: {self.score}", font=("Arial", 16), bg="black", fg="white")
        self.label.place(x=20, y=20)
        self.max_score_label = Label(root, text=f"Max Score: {self.max_score}", font=("Arial", 16), bg="black", fg="white")
        self.max_score_label.place(x=20, y=50)

    def update_score(self, points):
        self.score += points
        self.label.config(text=f"Score: {self.score}")
        if self.score > self.max_score:
            self.max_score = self.score
            self.max_score_label.config(text=f"Max Score: {self.max_score}")

    def reset_score(self):
        self.score = 0
        self.label.config(text=f"Score: {self.score}")

class Buttons:
    def __init__(self, root, display):
        self.root = root
        self.display = display
        self.create_buttons()

    def create_buttons(self):
        button_frame = Frame(self.root, bg='black')
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        button_frame.place(x=(screen_width - 150) // 2, y=screen_height - 150)

        # btn_up = Button(button_frame, text="↑", command=self.display.move_up, width=5, height=2)
        # btn_up.grid(row=0, column=1, padx=5, pady=5)
        #
        # btn_left = Button(button_frame, text="←", command=self.display.move_left, width=5, height=2)
        # btn_left.grid(row=1, column=0, padx=5, pady=5)
        #
        # btn_down = Button(button_frame, text="↓", command=self.display.move_down, width=5, height=2)
        # btn_down.grid(row=1, column=1, padx=5, pady=5)
        #
        # btn_right = Button(button_frame, text="→", command=self.display.move_right, width=5, height=2)
        # btn_right.grid(row=1, column=2, padx=5, pady=5)
        #
        # btn_restart = Button(button_frame, text="Restart", command=self.display.restart_game, width=10, height=2)
        # btn_restart.grid(row=2, column=0, columnspan=2, padx=5, pady=5)
        #
        # btn_close_game = Button(button_frame, text="Close", command=self.display.close_game, width=10, height=2)
        # btn_close_game.grid(row=2, column=3, columnspan=2, padx=5, pady=5)

def main():
    cell_size = 30
    matrics = Matrics()
    matricx = matrics.matrics
    print(matricx)

    root = Tk()
    root.title('Matrix Display 10x24')
    root.attributes('-fullscreen', True)
    root.configure(background='black')

    display = TkMatrixDisplay(root, matrics, cell_size)
    Buttons(root, display)

    root.bind('<Up>', display.move_up)
    root.bind('<Down>', display.move_down)
    root.bind('<Left>', display.move_left)
    root.bind('<Right>', display.move_right)
    root.bind('<Escape>', display.close_game)
    root.bind('<Return>', display.restart_game)

    def update_label():
        if display.matrics.ifempty():
            display.matrics.randomcreate()
        display.matrics.fall()
        display.show()
        display.iffullrow()
        display.matrics.endgame()
        root.after(10, update_label)

    update_label()

    root.mainloop()



