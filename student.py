from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
#main
class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1300x900")
        self.root.title("PresentinPy")
        self.root.resizable(False,False)

#front end codes here

#bg image
        img2=Image.open(r"D:\Work X Git\OOP 2 Project\Images\bg_home.png")
        img2=img2.resize((1300,700))
        self.photoimg2=ImageTk.PhotoImage(img2)

        bg_lbl=Label(self.root,image=self.photoimg2)
        bg_lbl.place(x=0,y=200,width=1300,height=700)

        title_lbl=Label(bg_lbl,text="Student Information",font=("arial",20,"bold"),bg="skyblue",fg="darkblue")
        title_lbl.place(x=550,y=00)

        main_frame=Frame(bg_lbl,bd=2,bg="white")
        main_frame.place(x=20,y=50,width="1250",height="600")

    #left label frame
        left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("arial",13,"bold"),fg="black")
        left_frame.place(x=15,y=10,width="600",height="570")

        #current course
        curent_course_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Information",font=("arial",13,"bold"),fg="black")
        curent_course_frame.place(x=30,y=30,width="570",height="300")
        #department
        dep_lebel=Label(curent_course_frame,text="Department",font=("arial",13,"bold"),bg="white",fg="black")
        dep_lebel.grid(row=0,column=0,padx=15,pady=5)

        dep_combo=ttk.Combobox(curent_course_frame,font=("arial",10),width="13",state="read only")
        dep_combo["values"]=("Select Department","Computer Science","IT","Civil")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=0,pady=10)

        #year
        yar_lebel=Label(curent_course_frame,text="Year",font=("arial",13,"bold"),bg="white",fg="black")
        yar_lebel.grid(row=0,column=2,padx=15,pady=5)

        yar_combo=ttk.Combobox(curent_course_frame,font=("arial",10),width="13",state="read only")
        yar_combo["values"]=("2020","2021","2022","2023","2024")
        yar_combo.current(0)
        yar_combo.grid(row=0,column=3,padx=0,pady=10)

        #batch
        batch_lebel=Label(curent_course_frame,text="Batch",font=("arial",13,"bold"),bg="white",fg="black")
        batch_lebel.grid(row=1,column=0,padx=0,pady=0)

        batch_combo=ttk.Combobox(curent_course_frame,font=("arial",10),width="13",state="read only")
        batch_combo["values"]=("2020","2021","2022","2023","2024")
        batch_combo.current(0)
        batch_combo.grid(row=1,column=1,padx=0,pady=0)

        #semester
        semester_lebel=Label(curent_course_frame,text="Semester",font=("arial",13,"bold"),bg="white",fg="black")
        semester_lebel.grid(row=1,column=2,padx=0,pady=0)

        semester_combo=ttk.Combobox(curent_course_frame,font=("arial",10),width="13",state="read only")
        semester_combo["values"]=("")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=0,pady=0)



    #right label frame
        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("arial",13,"bold"),fg="black")
        right_frame.place(x=630,y=10,width="600",height="570")



if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()