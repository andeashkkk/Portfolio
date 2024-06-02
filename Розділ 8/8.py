import tkinter as tk

# Створення головного вікна
app = tk.Tk()
app.title("Мій GUI")

# Додавання кнопки
button = tk.Button(app, text="Натисни мене")
button.pack()
button.config(font=("Arial", 12), fg="white", bg="blue")

# Додавання напису
label = tk.Label(app, text="Мій напис")
label.pack()
label.config(font=("Helvetica", 16), fg="black", bg="white")

# Додавання однорядкового текстового поля
entry = tk.Entry(app)
entry.pack()
entry.config(font=("Times New Roman", 14), fg="black", bg="white")

# Додавання багаторядкового текстового поля
text = tk.Text(app)
text.pack()
text.config(font=("Courier", 14), fg="purple", bg="pink")

# Додавання спадного списку
combo = tk.StringVar()
combo.set("Варіант 1")
combobox = tk.OptionMenu(app, combo, "Варіант 1", "Варіант 2", "Варіант 3")
combobox.pack()
combobox.config(font=("Arial", 12), fg="black", bg="lightblue")

# Додавання прапорця
checkbox = tk.Checkbutton(app, text="Прапорець")
checkbox.pack()
checkbox.config(fg="black")

# Додавання радіокнопок
radio_var = tk.IntVar()
radio1 = tk.Radiobutton(app, text="Вибір 1", variable=radio_var, value=1)
radio2 = tk.Radiobutton(app, text="Вибір 2", variable=radio_var, value=2)
radio1.pack()
radio2.pack()
radio1.config(fg="black", bg="lightgray")
radio2.config(fg="black", bg="lightgray")

# Функція для зміни відображення тексту
def change_text():
    label.config(text="Прізвище та ім'я: Страп Андріана")
    entry.insert(0, "Страп Андріана")
    text.insert(tk.END, "Страп Андріана")
    combo.set("Варіант Страп Андріана")

# Виклик функції для зміни тексту
change_text()

# Запуск програми
app.mainloop()
