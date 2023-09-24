from tkinter import *
from pack.just import *


def com():
    os.system("python win_write.py")


def search():
    global text
    df = pd.read_table("dian.txt", sep=",", names=["商品|条码", "生产日期", "保质期"])
    print(df, "\n")
    str_1 = ""
    for i in df.index:
        for j in df.iloc[i, :]:
            str_1 += str(j)
            str_1 += ","
        str_1 += iscode(df.at[i, "商品|条码"])
        str_1 += "\n"
        text.insert(INSERT, str_1)
        print(str_1)
        str_1 = ""


wi = Tk()
wi.title("主界面")
wi.geometry("600x550+400+200")
Button(wi, text="写入", command=com, font=("song ti", 16)).grid(row=0, column=0)
Button(wi, text="查询", command=search, font=("song ti", 16)).grid(row=1, column=0)
text = (Text(wi, width=60, height=15, font=("song ti", 12)))
text.grid(row=2, column=0)
wi.mainloop()
