def draw_line(length, direction, symbol):
    if not symbol or len(symbol) != 1:
        print("Ошибка: символ должен быть один.")
        return
    if direction.lower() == "горизонтальная":
        print(symbol * length)
    elif direction.lower() == "вертикальная":
        for _ in range(length):
            print(symbol)
    else:
        print("Ошибка: направление должно быть 'горизонтальная' или 'вертикальная'.")

draw_line(5, "горизонтальная", "*")
draw_line(3, "вертикальная", "#")
