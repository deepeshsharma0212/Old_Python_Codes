import tkinter as tk
root_window = tk.Tk()

frame1 = tk.Frame(root_window,bg='red')

def hello():
    r = tk.Tk()
    l1 = tk.Label(r,text='Hello World This is Awesome')
    b1 = tk.Button(r,text='exit',command=r.destroy)
    l1.grid(row=0,column=0)
    b1.grid(row=0,column=1)
    r.mainloop()
button1 = tk.Button(root_window,text='EXIT',command=root_window.destroy)
label1 = tk.Label(frame1,text='Hello World Welcome Tkinter GUI Design',fg='green',bg='yellow')

button2 = tk.Button(root_window,text='New_Window',command=hello)
button2.pack()

label1.pack()
frame1.pack()
button1.pack()
root_window.wm_minsize(500,300)
root_window.wm_maxsize(700,500)
root_window.wm_resizable(700,500)
root_window.title("MYAPPLICATION")
root_window.mainloop()
