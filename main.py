from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
#main
class Face_Rec_Sys:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1300x900")
        self.root.title("PresentinPy")

        img=Image.open(r"D:\Work X Git\OOP 2 Project\Images\banner.png")
        img=img.resize((1300,200))
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=1300,height=200)


if __name__ == "__main__":
    root=Tk()
    obj=Face_Rec_Sys(root)
    root.mainloop()