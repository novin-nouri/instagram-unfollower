from tkinter import *
from gui_tkinter import FirstScreen


if __name__ == "__main__":
    root = Tk()

    first_screen = FirstScreen(root)
    first_screen.add_logo()
    first_screen.add_image()
    first_screen.information()

    root.mainloop()