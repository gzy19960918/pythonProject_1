import os
import pandas as pd


def isdata(st):
    """
        创建一个函数来判断日期格式是否类似于20230122
        1. 首先判断字符串长度是否是8位数;
        2. 其次判断年份是否是2000年之后并在今年之前；
        3. 再次判断月份是否是1-12月；
        4. 最后判断日子是否符合自然规律。
    """
    # 存储年月日为整形数据
    day = int(st[6:])
    month = int(st[4:6])
    year = int(st[:4])
    # 开始逐条判断
    if len(st) != 8:
        return False
    if not 2000 <= year < 2024:
        return False
    if not 1 <= month <= 12:
        return False
    if day <= 0:
        return False
    if month in [1, 3, 5, 7, 8, 10, 12]:
        if day > 31:
            return False
    elif month == 2:
        if year % 4 != 0:
            if day >= 29:
                return False
        else:
            if day > 29:
                return False
    else:
        if day > 30:
            return False
    return True


def iscode(st):
    path = os.getcwd()
    path += "/表.xls"
    df = pd.read_excel(path, index_col=0)
    if st not in df.index:
        return False
    return df.loc[st, "名称"]


def month_or_day(st):
    return st[-1]
