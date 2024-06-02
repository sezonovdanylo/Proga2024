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
            if self.matrics.matrics[4] == [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0]]:
                self.matrics.end = False

    def move_up(self):
        self.matrics.centralpovorot()
        self.show()

    def move_down(self):
        self.matrics.figurefall()
        self.show()

    def move_left(self):
        self.matrics.left()
        self.show()

    def move_right(self):
        self.matrics.right()
        self.show()

class ScoreCounter:
    def __init__(self, root):
        self.root = root
        self.score = 0
        self.label = Label(root, text=f"Score: {self.score}", font=("Arial", 16), bg="black", fg="white")
        self.label.place(x=20, y=20)

    def update_score(self, points):
        self.score += points
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

        btn_up = Button(button_frame, text="↑", command=self.display.move_up, width=5, height=2)
        btn_up.grid(row=0, column=1, padx=5, pady=5)

        btn_left = Button(button_frame, text="←", command=self.display.move_left, width=5, height=2)
        btn_left.grid(row=1, column=0, padx=5, pady=5)

        btn_down = Button(button_frame, text="↓", command=self.display.move_down, width=5, height=2)
        btn_down.grid(row=1, column=1, padx=5, pady=5)

        btn_right = Button(button_frame, text="→", command=self.display.move_right, width=5, height=2)
        btn_right.grid(row=1, column=2, padx=5, pady=5)

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

    def update_label():
        if display.matrics.ifempty():
            display.matrics.randomcreate()
        display.matrics.fall()
        display.show()
        display.iffullrow()
        display.show()
        display.matrics.endgame()
        root.after(10, update_label)


    update_label()

    root.mainloop()

if __name__ == "__main__":
    main()


# Я знайшов деяку кількість незначних багів які не дуже якось ломають гру я доробив так щоб кнопки не оновлювались
