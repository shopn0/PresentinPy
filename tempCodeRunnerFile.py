from tkinter import*
from tkinter import tkk
from PIL import Image, ImageTk

class Face_Rec_Sys:
    def __init__(self,root):
        self.root=root
        self.root.geometry("600x900")
        self.root.title("PresentiPy")


if __name__ == "__main__":
    root=Tk()
    obj=Face_Rec_Sys(root)
    root.mainloop()