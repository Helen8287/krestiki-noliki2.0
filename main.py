import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window. title("Крестики - нолики")
window.geometry("300x400")


current_player = "X"
play_names = {"X": "Игрок 1", "0": "Игрок2"}
buttons = []

# Счетчики побед для каждого игрока
win_count = {"X": 0, "O": 0}

# Функция для проверки победителя
def check_winner ():
    for i in range (3):
        if buttons [i][0]["text"] == buttons [i][1] ["text"]== buttons [i][2]["text"] != "":
            return True
        if buttons [0][i]["text"] == buttons [1][i]["text"] == buttons [2][i]["text"]!= "":
            return True
    if  buttons [0][0]["text"] == buttons [1][1]["text"] == buttons [2][2]["text"]!= "":
        return True
    if buttons[0][2]["text"] == buttons[1][1] ["text"]== buttons[2][0]["text"]!= "":
        return True

    return False

# Функция  проверяет, заполнены ли все кнопки, что указывает на ничью.
def check_draw():
    for row in buttons:
        for btn in row:
            if btn["text"] == "":
                return False
    return True


# Функция, срабатывающая при нажатии на кнопку. Управляет ходами игроков и проверяет условия победы или ничьей.
def on_click( row, col ):
    global current_player

    if buttons [row] [col] ['text'] != "":
        return

    buttons[row] [col] ['text'] = current_player

    if check_winner():
        win_count[current_player] += 1
        messagebox.showinfo("Игра окончена", f"Игрок {current_player} победил!")
        if not counter_game():
            reset_game()
    elif check_draw():
        messagebox.showinfo("Вы оба молодцы!","Получилась ничья!")
        reset_game()
    else:
        current_player = "0" if current_player == "X" else "X"


# Функция сбрасывает состояние игры для нового раунда.
def reset_game():
    global current_player
    current_player = "X"
    for row in buttons:
        for btn in row:
            btn["text"] = ""


# Функция для проверки количества побед и завершения игры, если один из игроков достиг трех побед.
def counter_game():
    for player, count in win_count.items():
        if count == 3:
            messagebox.showinfo("Игра завершена", f"Игрок {player_names[player]} выиграл 3 раза и победил в матче!")
            window.quit()
            return True
    return False


# Функция для установки имен игроков
def set_player_names():
    global play_names
    play_names["X"] = player1_entry.get() or "Игрок 1"
    play_names["O"] = player2_entry.get() or "Игрок 2"
    player1_entry.config(state='disabled')
    player2_entry.config(state='disabled')
    start_button.config(state='disabled')


# Создание полей для ввода имен игроков
player1_label = tk.Label(window, text="Имя Игрока 1 (X):")
player1_label.grid(row = 0, column = 0, columnspan = 3)

player1_entry = tk.Entry(window)
player1_entry.grid(row = 1, column = 0, columnspan = 3)

player2_label = tk.Label(window, text="Имя Игрока 2 (O):")
player2_label.grid(row = 2, column = 0, columnspan = 3)

player2_entry = tk.Entry(window)
player2_entry.grid(row = 3, column = 0, columnspan = 3)

start_button = tk.Button(window, text="Начать игру", command=set_player_names)
start_button.grid(row = 4, column = 0, columnspan = 3)

# Создание кнопок для игры.Смещение строки на 5 вниз из-за вводов
for i in range(3):
    row = []
    for j in range(3):
        btn = tk.Button(window, text = "", font = ("Arial",20), width = 5, height = 2, command= lambda r = i, c = j: on_click(r,c))
        btn.grid(row = i+5, column = j)
        row.append(btn)
    buttons.append(row)


window.mainloop()