import tkinter as tk

def calculate(event=None):
    try:
        bill = float(entry.get())
        tip_percent = scale.get()

        tip = bill * tip_percent / 100
        total = bill + tip

        result_label.config(
            text=f"Чаевые: {tip:.2f} ₽\nИтого: {total:.2f} ₽"
        )
    except:
        result_label.config(text="Введите число!")

window = tk.Tk()
window.title("Личный кассир")
window.geometry("300x200")

tk.Label(window, text="Сумма счета:").pack()
entry = tk.Entry(window)
entry.pack()

scale = tk.Scale(window, from_=5, to=25, orient="horizontal", label="Чаевые (%)", command=calculate)
scale.pack()

result_label = tk.Label(window, text="")
result_label.pack()

window.mainloop()

#2 задание не  понял как делать
