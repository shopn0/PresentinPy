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

#user_buttons
        img3=Image.open(r"D:\Work X Git\OOP 2 Project\Images\attendance.png")
        img3=img3.resize((200,200))
        self.photoimg3=ImageTk.PhotoImage(img3)

        b1=Button(bg_lbl,image=self.photoimg3,cursor="hand2")
        b1.place(x=100,y=200,width=200,height=200)
        b1_t=Button(bg_lbl,text="Attendance",cursor="hand2",font=("arial",20,"bold"),bg="skyblue",fg="darkblue")
        b1_t.place(x=100,y=400,width=200,height=30)

    #button 2 - Face detector

        img4=Image.open(r"D:\Work X Git\OOP 2 Project\Images\face.png")
        img4=img4.resize((200,200))
        self.photoimg4=ImageTk.PhotoImage(img4)

        b2=Button(bg_lbl,image=self.photoimg4,cursor="hand2")
        b2.place(x=400,y=200,width=200,height=200)
        b2_t=Button(bg_lbl,text="Face Detector",cursor="hand2",font=("arial",20,"bold"),bg="skyblue",fg="darkblue")
        b2_t.place(x=400,y=400,width=200,height=30)

if __name__ == "__main__":
    root=Tk()
    obj=Face_Rec_Sys(root)
    root.mainloop()