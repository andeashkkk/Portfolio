import tkinter as tk
from tkinter import ttk
import sqlite3

app = tk.Tk()
app.title("Страп Андріана Група 2 ЛР №2")
app.geometry("900x400")

db_connection = sqlite3.connect("pol_lab02.s3db")
db_cursor = db_connection.cursor()

db_cursor.execute(f"SELECT sgn FROM tnoun WHERE sgN LIKE 't%' LIMIT 1")
result = db_cursor.fetchone()

frame = tk.Frame(app)
frame.pack(pady=10)
label_result = tk.Label(frame, text="Слово в початковій формі (sgN):")
if result:
    label_result.config(text="Слово в початковій формі (sgN) на букву T: " + result[0])
else:
    label_result.config(text="Слово не знайдено")

button = tk.Button(frame, text="Натисни мене")

tree = ttk.Treeview(frame, columns=("ID", "Словоформа (sgN)", "Словоформа (інший відмінок)"), height=12)
tree.heading("#1", text="ID")
tree.heading("#2", text="Словоформа (sgN)")
tree.heading("#3", text="Словоформа (інший відмінок)")
tree.column('#0', minwidth=0, width=0)
tree.column("#1", anchor="center")
tree.column("#2", anchor="center")
tree.column("#3", anchor="center")

combo = ttk.Combobox(frame)
combo.set("Оберіть опцію")
def fetch_and_display_data():
    db_cursor.execute("SELECT id, sgN, plD FROM tnoun LIMIT 12")
    data = db_cursor.fetchall()

    # Завдання 6
    # for row in data:
    #     tree.insert("", "end", values=row) 
   
    for i, row in enumerate(data):
        # Завдання 7
        # tree.insert("", "end", values=(i + 1, row[1], row[2]))

        # Завдання 8
        tree.insert("", "end", values=(i + 1, row[1], row[2] if row[2] else "-"))
        
    # Завдання 9
    db_cursor.execute(f"SELECT sgn FROM tnoun WHERE sgN LIKE 't%'")
    data = db_cursor.fetchall()
    combo.config(values=data)
    
button.config(command=fetch_and_display_data)
label_result.pack()
button.pack()
combo.pack()
tree.pack()

app.mainloop()
db_connection.close()
