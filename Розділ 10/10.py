import tkinter as tk
from tkinter import ttk
import sqlite3

# Підключення до бази даних (створення або відкриття існуючої)
conn = sqlite3.connect('dictionary.db')
cursor = conn.cursor()

# Створення таблиці vocab
cursor.execute('''
    CREATE TABLE IF NOT EXISTS vocab (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        category TEXT,
        foreign_word TEXT,
        translation TEXT
    )
''')

# Додавання даних до таблиці
data = [
    ('Кольори', 'Rood', 'Червоний'),
    ('Предмети', 'Tafel', 'Стіл'),
    ('Кольори', 'Blauw', 'Синій'),
    ('Предмети', 'Stoel', 'Стілець'),
    ('Фрукти', 'Appel', 'Яблуко'),
    ('Фрукти', 'Banaan', 'Банан'),
    ('Транспорт', 'Auto', 'Автомобіль'),
    ('Транспорт', 'Fiets', 'Велосипед'),
    ('Тварини', 'Hond', 'Собака'),
    ('Тварини', 'Kat', 'Кіт'),
    ('Країни', 'USA', 'Сполучені Штати Америки'),
    ('Країни', 'Frankrijk', 'Франція'),
    ('Кольори', 'Groen', 'Зелений'),
    ('Фрукти', 'Sinaasappel', 'Апельсин'),
    ('Транспорт', 'Trein', 'Поїзд'),
    ('Тварини', 'Olifant', 'Слон'),
    ('Країни', 'Japan', 'Японія'),
    ('Предмети', 'Lamp', 'Лампа'),
    ('Країни', 'Brazilië', 'Бразилія'),
    ('Кольори', 'Geel', 'Жовтий'),
    ('Кольори', 'Oranje', 'Оранжевий'),
    ('Транспорт', 'Bus', 'Автобус'),
    ('Транспорт', 'Vliegtuig', 'Літак'),
    ('Тварини', 'Koe', 'Корова'),
    ('Тварини', 'Vogel', 'Птах'),
    ('Фрукти', 'Perzik', 'Персик'),
    ('Фрукти', 'Peer', 'Груша'),
    ('Предмети', 'Boek', 'Книга'),
    ('Країни', 'Duitsland', 'Німеччина'),
    ('Країни', 'Spanje', 'Іспанія'),
    ('Кольори', 'Paars', 'Фіолетовий'),
    ('Кольори', 'Bruin', 'Коричневий'),
    ('Транспорт', 'Motorfiets', 'Мотоцикл'),
    ('Транспорт', 'Boot', 'Човен'),
    ('Тварини', 'Haas', 'Заєць'),
    ('Тварини', 'Leeuw', 'Лев'),
    ('Фрукти', 'Kiwi', 'Ківі'),
    ('Фрукти', 'Mango', 'Манго'),
    ('Предмети', 'Klok', 'Годинник'),
    ('Предмети', 'Sleutel', 'Ключ'),
    ('Країни', 'Canada', 'Канада'),
    ('Країни', 'China', 'Китай'),
    ('Кольори', 'Zwart', 'Чорний'),
    ('Кольори', 'Wit', 'Білий'),
    ('Транспорт', 'Metro', 'Метро'),
    ('Транспорт', 'Tram', 'Трамвай'),
    ('Тварини', 'Vis', 'Риба'),
    ('Тварини', 'Slang', 'Змія'),
    ('Фрукти', 'Ananas', 'Ананас'),
    ('Фрукти', 'Druif', 'Виноград'),
    ('Предмети', 'Telefoon', 'Телефон'),
    ('Предмети', 'Tas', 'Сумка'),
    ('Країни', 'Nederland', 'Нідерланди'),
    ('Країни', 'India', 'Індія'),
    ('Кольори', 'Roze', 'Рожевий')
]

cursor.executemany('INSERT INTO vocab(category, foreign_word, translation) VALUES (?, ?, ?)', data)

conn.commit()
conn.close()

import tkinter as tk
from tkinter import ttk
import sqlite3

def load_words(event=None):
    selected_category = combo_category.get()
    tree.delete(*tree.get_children())
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    if selected_category:
        words = cursor.execute('SELECT * FROM vocab WHERE category=? ORDER BY foreign_word', (selected_category,)).fetchall()
        for word in words:
            tree.insert('', 'end', values=word)
    else:
        words = cursor.execute('SELECT * FROM vocab ORDER BY foreign_word').fetchall()
        for word in words:
            tree.insert('', 'end', values=word)
    conn.close()

def on_cell_select(event):
    selected_row = tree.selection()
    if selected_row:
        selected_item = tree.item(selected_row, 'values')
        if selected_item:
            selected_foreign_word = selected_item[2]
            selected_translation = selected_item[3]
            label_word_translation.config(text=f"{selected_foreign_word} - {selected_translation}")

db_path = 'dictionary.db'
conn = sqlite3.connect(db_path)
cursor = conn.cursor()
root = tk.Tk()
root.title("Страп Андріана Група 2 ЛР №3")

notebook = ttk.Notebook(root)
notebook.pack(pady=10)

tab_dictionary = ttk.Frame(notebook)
notebook.add(tab_dictionary, text='Словник')

label_instruction = tk.Label(tab_dictionary, text="Виберіть категорію:")
label_instruction.grid(row=0, column=0, padx=10, pady=10)

categories = [row[0] for row in cursor.execute('SELECT DISTINCT category FROM vocab').fetchall()]
combo_category = ttk.Combobox(tab_dictionary, values=categories)
combo_category.grid(row=0, column=1, padx=10, pady=10)

combo_category.bind('<<ComboboxSelected>>', load_words)

tree = ttk.Treeview(tab_dictionary, columns=('ID', 'Category', 'Foreign Word', 'Translation'), show='headings', height=15)
tree.heading('ID', text='ID')
tree.heading('Category', text='Category')
tree.heading('Foreign Word', text='Слово (іноземна мова)')
tree.heading('Translation', text='Переклад (українська мова)')
tree.column('ID', anchor='center')
tree.column('Category', anchor='center')
tree.column('Foreign Word', anchor='center')
tree.column('Translation', anchor='center')
tree.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

tree_scroll_y = ttk.Scrollbar(tab_dictionary, command=tree.yview)
tree_scroll_y.grid(row=1, column=2, sticky='ns')
tree.configure(yscrollcommand=tree_scroll_y.set)

tree.bind('<ButtonRelease-1>', on_cell_select)

label_word_translation = tk.Label(tab_dictionary, text="", font=('Arial', 14, 'bold'), pady=10)
label_word_translation.grid(row=2, column=0, columnspan=2)

load_words()

tab_author = ttk.Frame(notebook)
notebook.add(tab_author, text='Про автора')

label_author_info = tk.Label(tab_author, text="Страп Андріана\nГрупа 2")
label_author_info.config(font=('Arial', 16, 'bold'), justify='center')
label_author_info.pack(pady=50)

conn.close()

root.mainloop()
