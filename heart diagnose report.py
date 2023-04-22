from tkinter import *
from tkinter import messagebox
root = Tk()
root.title("Heart Diagnose Report")
root.geometry("600x600")

question1_radiobutton = StringVar(value="0")

q1=Label(root, text="Do you experience shortness of breath during routine activities ? ")
q1.pack()
q1r1 = Radiobutton(root, text="yes", variable=question1_radiobutton, value="yes")
q1r1.pack()
q1r2 = Radiobutton(root, text="no", variable=question1_radiobutton, value="no")
q1r2.pack()

question2_radiobutton = StringVar(value="0")

q2=Label(root, text="Do you have swelling in the feet/ ankles/ legs(shoes feel tighter) or abdomen?")
q2.pack()
q2r1 = Radiobutton(root, text="yes", variable=question2_radiobutton, value="yes")
q2r1.pack()
q2r2 = Radiobutton(root, text="no", variable=question2_radiobutton, value="no")
q2r2.pack()

question3_radiobutton = StringVar(value="0")

q3=Label(root, text="Do you feel any of these symptoms - confusion,disorientation or loss of memory?")
q3.pack()
q3r1 = Radiobutton(root, text="yes", variable=question3_radiobutton, value="yes")
q3r1.pack()
q3r2 = Radiobutton(root, text="no", variable=question3_radiobutton, value="no")
q3r2.pack()

question4_radiobutton = StringVar(value="0")

q4=Label(root, text="Do you experience shortness of breath while at rest /lying down?")
q4.pack()
q4r1 = Radiobutton(root, text="yes", variable=question4_radiobutton, value="yes")
q4r1.pack()
q4r2 = Radiobutton(root, text="no", variable=question4_radiobutton, value="no")
q4r2.pack()

question5_radiobutton = StringVar(value="0")

q5=Label(root, text="Do you experience persistent wheezing /coughing that produces white or pink blood tinged mucus ?")
q5.pack()
q5r1 = Radiobutton(root, text="yes", variable=question5_radiobutton, value="yes")
q5r1.pack()
q5r2 = Radiobutton(root, text="no", variable=question5_radiobutton, value="no")
q5r2.pack()

def report():
    score=0
    
    if question1_radiobutton.get()=="yes":
        score=score+20
        
    if question2_radiobutton.get()=="yes":
        score=score+20
        
    if question3_radiobutton.get()=="yes":
        score=score+20
        
    if question4_radiobutton.get()=="yes":
        score=score+20
        
    if question5_radiobutton.get()=="yes":
        score=score+20
        
    print(score)
    
    if score<=40:
        messagebox.showinfo("report","you don't need to visit a doctor")
        
    elif score<=60:
        messagebox.showinfo("report","you might perhaps visit a doctor")
        
    else :
        messagebox.showinfo("report","I strongly advise you to visit a doctor")
        
button = Button(root, text="Click here", command=report)
button.pack()

        
root.mainloop()
