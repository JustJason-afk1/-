#задание 1 
import tkinter as tk

def calculate(event=None):
    try:
        bill = float(entry_bill.get())
        percent = scale.get()

        tips = bill * percent / 100
        total = bill + tips

        result.config(text=f"Чаевые: {tips:.2f} руб.\nИтого: {total:.2f} руб.")
    except:
        result.config(text="Введите сумму счета")


window = tk.Tk()
window.title("Личный кассир")
window.geometry("350x250")

label_bill = tk.Label(window, text="Сумма счета:")
label_bill.pack(pady=5)

entry_bill = tk.Entry(window)
entry_bill.pack()

label_percent = tk.Label(window, text="Процент чаевых:")
labelpercent.pack(pady=5)

scale = tk.Scale(window, from=5, to=25, orient="horizontal",
                 command=calculate)
scale.set(10)
scale.pack()

result = tk.Label(window, text="Чаевые: 0 руб.\nИтого: 0 руб.")
result.pack(pady=15)

window.mainloop()


#задание 2
import tkinter as tk

def calculate():
    if size.get() == 1:
        price = 100
    elif size.get() == 2:
        price = 200
    else:
        price = 300

    if cheese.get():
        price += 30

    if mushrooms.get():
        price += 30

    if sausage.get():
        price += 30

    result.config(text=f"Итоговая цена: {price} руб.")


window = tk.Tk()
window.title("Пицерия")
window.geometry("350x350")

label_size = tk.Label(window, text="Выберите размер пиццы:")
label_size.pack(pady=5)

size = tk.IntVar()
size.set(1)

small = tk.Radiobutton(window, text="Маленькая - 100 руб.",
                       variable=size, value=1)
small.pack()

medium = tk.Radiobutton(window, text="Средняя - 200 руб.",
                        variable=size, value=2)
medium.pack()

big = tk.Radiobutton(window, text="Большая - 300 руб.",
                     variable=size, value=3)
big.pack()

label_add = tk.Label(window, text="Добавки:")
label_add.pack(pady=10)

cheese = tk.BooleanVar()
mushrooms = tk.BooleanVar()
sausage = tk.BooleanVar()

check_cheese = tk.Checkbutton(window, text="Сыр +30 руб.",
                              variable=cheese)
check_cheese.pack()

check_mushrooms = tk.Checkbutton(window, text="Грибы +30 руб.",
                                 variable=mushrooms)
check_mushrooms.pack()

check_sausage = tk.Checkbutton(window, text="Колбаса +30 руб.",
                               variable=sausage)
check_sausage.pack()

button = tk.Button(window, text="Рассчитать", command=calculate)
button.pack(pady=15)

result = tk.Label(window, text="Итоговая цена: 0 руб.")
result.pack()

window.mainloop()
