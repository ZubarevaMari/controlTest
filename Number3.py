# Зубарева Мария Олеговна
# 44-22-122, вариант 12, №3
import math
import tkinter as tk

nums = []


def func(args):
    res = []
    if len(args) == 0:
        print("Ошибка. Строка пустая")
        return None
    for x in args:
        if type(x) != int and type(x) != float:
            print("Ошибка. Необходимо ввести число")
            return None
        if x < 1:
            y = math.sin(x + x ** 2)
        elif x >= 1:
            y = x * (x + 0.3) ** (1 / 2)
        res.append(y)
    return res


def changeNum():
    nums = list()
    try:
        nums = [int(i) for i in entry.get().split(" ")]
        new_num = func(nums)
        lbl_value["text"] = f"{new_num}"
    except:
        new_num = "Ошибка при вводе"
        lbl_value["text"] = f"{new_num}"


window = tk.Tk()
window.title("Преобразоатель чисел")
window.rowconfigure([0, 1, 2], minsize=50, weight=1)
window.columnconfigure([0, 1], minsize=50, weight=1)

lbl_entry = tk.Label(master=window, text="Введите числа:")
lbl_entry.grid(row=0, column=0, padx=5)
entry = tk.Entry(fg="black", bg="white", width=25)
entry.grid(row=0, column=1,  padx=10)

btn_enter = tk.Button(master=window, text="Преобразовать", foreground="black",
                      background="red", command=changeNum)
btn_enter.grid(row=1, columnspan=3, padx=10)

lbl_answer = tk.Label(master=window, text="Ответ:")
lbl_answer.grid(row=2, column=0, padx=10)
lbl_value = tk.Label(master=window, text="0")
lbl_value.grid(row=2, column=1, padx=10)

window.mainloop()