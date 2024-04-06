from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
#main
class Face_Rec_Sys:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1300x900")
        self.root.title("PresentinPy")
        self.root.resizable(False,False)
#Heading banner x logo / intro
        img=Image.open(r"D:\Work X Git\OOP 2 Project\Images\banner.png")
        img=img.resize((1300,200))
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=1300,height=200)
#bg image
        img2=Image.open(r"D:\Work X Git\OOP 2 Project\Images\bg_home.png")
        img2=img2.resize((1300,700))
        self.photoimg2=ImageTk.PhotoImage(img2)

        bg_lbl=Label(self.root,image=self.photoimg2)
        bg_lbl.place(x=0,y=200,width=1300,height=700)


if __name__ == "__main__":
    root=Tk()
    obj=Face_Rec_Sys(root)
    root.mainloop()