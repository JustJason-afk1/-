import tkinter as tk
import random

jokes = [
    "— Доктор, я буду жить? — А смысл?",
    "Программист умер и попал в ад... а там Wi-Fi без пароля!",
    "Учитель: объясни что такое ошибка. Студент: это когда всё работает, но ты не знаешь почему.",
    "Купил компьютер — теперь у меня 1% знаний и 99% обновлений.",
    "— Ты где? — Я в коде, не трогай меня."
]

def show_joke():
    label.config(text=random.choice(jokes))

window = tk.Tk()
window.title("Анекдоты")
window.geometry("400x200")

label = tk.Label(window, text="Нажми кнопку, чтобы получить анекдот",
                  wraplength=350, font=("Arial", 12))
label.pack(pady=20)

btn = tk.Button(window, text="Случайный анекдот", command=show_joke)
btn.pack()

window.mainloop()
