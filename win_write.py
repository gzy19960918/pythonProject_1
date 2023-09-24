from tkinter import *

win = Tk()
win.title("输入信息")
win.geometry("320x300+300+100")


def write():
    st_1 = e_1.get()
    st_2 = e_2.get()
    st_3 = e_3.get()
    with open("dian.txt", "a") as f:
        f.write(st_1)
        f.write(",")
        f.write(st_2)
        f.write(",")
        f.write(st_3)
        f.write("\n")
        e_1.delete(0, END)
        e_2.delete(0, END)
        e_3.delete(0, END)


Label(win, text="商品编码:", font=("song ti", 14), width=10, height=3).grid(row=0, column=0)
e_1 = Entry(win, font=("song ti", 14))
e_1.grid(row=0, column=1)
Label(win, text="生产日期:", font=("song ti", 14), width=10, height=3).grid(row=1, column=0)
e_2 = Entry(win, font=("song ti", 14))
e_2.grid(row=1, column=1)
Label(win, text="商品编码:", font=("song ti", 14), width=10, height=3).grid(row=2, column=0)
e_3 = Entry(win, font=("song ti", 14))
e_3.grid(row=2, column=1)
Button(win, text="写入", command=write, font=("song ti", 14)).grid(row=3, column=1)
win.mainloop()
