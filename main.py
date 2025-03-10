import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk


# Создание основного окна приложения
window = tk.Tk()
window.title("Крестики - нолики")
window.geometry("1200x800")



def create_background_image():
    # Загрузите фоновое изображение
    image = Image.open("image/3840x2160.jpg")

    # Изменяем размер изображения
    img_resized = image.resize((1200, 800))

    # Преобразуем изображение в формат, который может использовать Tkinter
    return ImageTk.PhotoImage(img_resized)



# Создание холста для фонового изображения
canvas = tk.Canvas(window, width=1200, height=800)
canvas.pack(expand=True, fill='both')  # Создаем холст для изображения


# Установка фонового изображения на холст
bg_image = create_background_image()  # Получаем подготовленное изображение
canvas.create_image(0, 0, image=bg_image, anchor='nw')  # Размещаем изображение в окне


# Переменная для хранения текущего игрока
current_player = "X"  # Первый игрок
play_names = {"X": "Игрок 1", "O": "Игрок 2"}  # Словарь для хранения имен игроков
buttons = []  # Список для хранения кнопок игрового поля


# Счетчики побед для каждого игрока
win_count = {"X": 0, "O": 0}



# Функция для проверки победителя
def check_winner():
    for i in range(3):
        if buttons[i][0]["text"] == buttons[i][1]["text"] == buttons[i][2]["text"] != "":
            return True
        if buttons[0][i]["text"] == buttons[1][i]["text"] == buttons[2][i]["text"] != "":
            return True
    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        return True
    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        return True

    return False



# Функция  проверяет, заполнены ли все кнопки и нет победителя, что указывает на ничью.
def check_draw():
    for row in buttons:
        for btn in row:
            if btn["text"] == "":
                return False
    return True



# Функция, срабатывающая при нажатии на кнопку. Управляет ходами игроков и проверяет условия победы или ничьей.
def on_click(row, col):
    global current_player

    if buttons[row][col]['text'] != "":  # Если кнопка уже нажата, ничего не делаем
        return


    buttons[row][col]['text'] = current_player  # Устанавливаем текст кнопки в символ текущего игрока


    # Проверяем условия победы или ничьей
    if check_winner():
        win_count[current_player] += 1
        messagebox.showinfo("Игра окончена", f"Игрок {current_player} победил!")
        if not counter_game():
            reset_game()
    elif check_draw():
        messagebox.showinfo("Вы оба молодцы!", "Получилась ничья!")
        reset_game()
    else:
        current_player = "O" if current_player == "X" else "X"  # Переключаем игрока




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
            messagebox.showinfo("Игра завершена", f"Игрок {play_names[player]} выиграл 3 раза и победил в матче!")
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



# Создание фрейма для игрового окна
game_frame = tk.Frame(window, width=300, height=400)
game_frame.place(relx=0.5, rely=0.6, anchor='center')



# Создание кнопок для игры
for i in range(3):
    row_buttons = []
    for j in range(3):
        btn = tk.Button(game_frame, text="", font=('Arial', 40), width=5, height=2,
                        command=lambda row=i, col=j: on_click(row, col))
        btn.grid(row=i, column=j)   # Размещаем кнопку
        row_buttons.append(btn)   # Добавляем кнопку в строку
    buttons.append(row_buttons)  # Добавляем строку в список кнопок




# Создание полей для ввода имен игроков
player1_label = tk.Label(window, text="Имя Игрока 1 (X):")
player1_label.place(relx=0.5, rely=0.1, anchor='center')
player1_entry = tk.Entry(window)
player1_entry.place(relx=0.5, rely=0.15, anchor='center')

player2_label = tk.Label(window, text="Имя Игрока 2 (O):")
player2_label.place(relx=0.5, rely=0.2, anchor='center')
player2_entry = tk.Entry(window)
player2_entry.place(relx=0.5, rely=0.25, anchor='center')

start_button = tk.Button(window, text="Начать игру", command=set_player_names)
start_button.place(relx=0.5, rely=0.3, anchor='center')


window.mainloop()




