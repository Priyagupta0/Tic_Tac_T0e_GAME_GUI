import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.geometry("510x550")
window.title("Tic Tac Toe\tPlayer1 : X \tPlayer2 : 0")

def checkwhowon():
    
    if b1["text"]=="X" and b2["text"]=="X" and b3["text"]=="X":
        b1.configure(bg="green")
        b2.configure(bg="green")
        b3.configure(bg="green")
        messagebox.showinfo(title="tic Tac Toe", message=" X won the match ")
    elif b4["text"]=="X" and b5["text"]=="X" and b6["text"]=="X":
        b4.configure(bg="green")
        b5.configure(bg="green")
        b6.configure(bg="green")
        messagebox.showinfo(title="tic Tac Toe", message=" X won the match ")
    elif b7["text"]=="X" and b8["text"]=="X" and b9["text"]=="X":
        b7.configure(bg="green")
        b8.configure(bg="green")
        b9.configure(bg="green")
        messagebox.showinfo(title="tic Tac Toe", message=" X won the match ")
    elif b1["text"]=="X" and b4["text"]=="X" and b7["text"]=="X":
        b1.configure(bg="green")
        b4.configure(bg="green")
        b7.configure(bg="green")
        messagebox.showinfo(title="tic Tac Toe", message=" X won the match ")   
    elif b2["text"]=="X" and b5["text"]=="X" and b8["text"]=="X":
        b2.configure(bg="green")
        b5.configure(bg="green")
        b8.configure(bg="green")
        messagebox.showinfo(title="tic Tac Toe", message=" X won the match ")     
    elif b3["text"]=="X" and b6["text"]=="X" and b9["text"]=="X":
        b3.configure(bg="green")
        b6.configure(bg="green")
        b9.configure(bg="green")
        messagebox.showinfo(title="tic Tac Toe", message=" X won the match ")  
    elif b1["text"]=="X" and b5["text"]=="X" and b9["text"]=="X":
        b1.configure(bg="green")
        b5.configure(bg="green")
        b9.configure(bg="green")
        messagebox.showinfo(title="tic Tac Toe", message=" X won the match ")
    elif b3["text"]=="X" and b5["text"]=="X" and b7["text"]=="X":
        b3.configure(bg="green")
        b5.configure(bg="green")
        b7.configure(bg="green")
        messagebox.showinfo(title="tic Tac Toe", message=" X won the match ")
    elif b1["text"]=="0" and b2["text"]=="0" and b3["text"]=="0":
        b1.configure(bg="green")
        b2.configure(bg="green")
        b3.configure(bg="green")
        messagebox.showinfo(title="tic Tac Toe", message=" 0 won the match ")
    elif b4["text"]=="0" and b5["text"]=="0" and b6["text"]=="0":
        b4.configure(bg="green")
        b5.configure(bg="green")
        b6.configure(bg="green")
        messagebox.showinfo(title="tic Tac Toe", message=" 0 won the match ")
    elif b7["text"]=="0" and b8["text"]=="0" and b9["text"]=="0":
        b7.configure(bg="green")
        b8.configure(bg="green")
        b9.configure(bg="green")
        messagebox.showinfo(title="tic Tac Toe", message=" 0 won the match ")
    elif b1["text"]=="0" and b4["text"]=="0" and b7["text"]=="0":
        b1.configure(bg="green")
        b4.configure(bg="green")
        b7.configure(bg="green")
        messagebox.showinfo(title="tic Tac Toe", message=" 0 won the match ")   
    elif b2["text"]=="0" and b5["text"]=="0" and b8["text"]=="0":
        b2.configure(bg="green")
        b5.configure(bg="green")
        b8.configure(bg="green")
        messagebox.showinfo(title="tic Tac Toe", message=" 0 won the match ")     
    elif b3["text"]=="0" and b6["text"]=="0" and b7["text"]=="0":
        b3.configure(bg="green")
        b6.configure(bg="green")
        b7.configure(bg="green")
        messagebox.showinfo(title="tic Tac Toe", message=" 0 won the match ")  
    elif b1["text"]=="0" and b5["text"]=="0" and b9["text"]=="0":
        b1.configure(bg="green")
        b5.configure(bg="green")
        b9.configure(bg="green")
        messagebox.showinfo(title="tic Tac Toe", message=" 0 won the match ")
    elif b3["text"]=="0" and b5["text"]=="0" and b7["text"]=="0":
        b3.configure(bg="green")
        b5.configure(bg="green")
        b7.configure(bg="green")
        messagebox.showinfo(title="tic Tac Toe", message=" 0 won the match ")
    elif count==9:
        messagebox.showinfo(title="tic Tac Toe", message=" Match Draw ")
    
# If x start
clicked = True
count = 0

def b_click(b):
    global clicked,count
    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count = count + 1
        checkwhowon()
    if b["text"] == " " and clicked == False:
        b["text"] = "0"
        clicked = True
        count = count + 1


b1= tk.Button(text=" ", font=("Helvetica",20), height=5, width=10, command=lambda:b_click(b1))
b1.grid(row=0, column=0)

b2= tk.Button(text=" ", font=("Helvetica",20), height=5, width=10, command=lambda:b_click(b2))
b2.grid(row=0, column=1)

b3= tk.Button(text=" ", font=("Helvetica",20), height=5, width=10, command=lambda:b_click(b3))
b3.grid(row=0, column=2)

b4= tk.Button(text=" ", font=("Helvetica",20), height=5, width=10, command=lambda:b_click(b4))
b4.grid(row=1, column=0)

b5= tk.Button(text=" ", font=("Helvetica",20), height=5, width=10, command=lambda:b_click(b5))
b5.grid(row=1, column=1)

b6= tk.Button(text=" ", font=("Helvetica",20), height=5, width=10, command=lambda:b_click(b6))
b6.grid(row=1, column=2)

b7= tk.Button(text=" ", font=("Helvetica",20), height=5, width=10, command=lambda:b_click(b7))
b7.grid(row=2, column=0)

b8= tk.Button(text=" ", font=("Helvetica",20), height=5, width=10, command=lambda:b_click(b8))
b8.grid(row=2, column=1)

b9= tk.Button(text=" ", font=("Helvetica",20), height=5, width=10, command=lambda:b_click(b9))
b9.grid(row=2, column=2)


window.mainloop()