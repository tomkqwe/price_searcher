import pandas as pd
import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox

# Глобальная переменная для хранения выбранного файла
selected_file = None


# Функция для чтения файла Excel
def read_xls(file):
    return pd.read_excel(file, header=13)


# Функция для выбора файла
def select_file():
    global selected_file
    file_path = filedialog.askopenfilename(
        title="Выберите Excel файл",
        filetypes=[("Excel файлы", "*.xls *.xlsx")]
    )

    if file_path:
        selected_file = file_path
        messagebox.showinfo("Файл выбран", f"Выбран файл: {file_path}")
    else:
        messagebox.showerror("Ошибка", "Файл не выбран!")


# Функция для поиска по строке
def search_in_file():
    global selected_file
    if not selected_file:
        messagebox.showerror("Ошибка", "Файл не выбран! Пожалуйста, выберите файл сначала.")
        return

    # Запрос строки для поиска
    search_term = simpledialog.askstring("Поиск", "Введите строку для поиска в столбце 'Наименование':")
    if not search_term:
        messagebox.showerror("Ошибка", "Строка для поиска не введена!")
        return

    # Чтение и обработка файла
    try:
        sheets1 = read_xls(selected_file)
        sheets1 = sheets1.loc[:, ~sheets1.columns.str.contains('^Unnamed')]
        res = sheets1.dropna(thresh=4)

        # Поиск строки с указанной подстрокой
        row = res[res['Наименование'].str.contains(search_term, na=False)]

        # Если строки найдены, выводим их в новом окне с возможностью копирования
        if not row.empty:
            result_text = row.to_string(index=False)
            show_result_window(result_text)
        else:
            messagebox.showinfo("Результат", "Совпадений не найдено.")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Произошла ошибка: {e}")


# Функция для отображения результата в отдельном окне
def show_result_window(result_text):
    result_window = tk.Toplevel()
    result_window.title("Результаты поиска")

    # Текстовое поле для отображения результата
    text_area = tk.Text(result_window, wrap="word", height=20, width=80)
    text_area.insert(tk.END, result_text)
    text_area.config(state=tk.NORMAL)  # Позволяет выделять и копировать текст
    text_area.pack(pady=10, padx=10)

    # Функция для копирования выделенного текста в буфер обмена
    def copy_to_clipboard():
        selected_text = text_area.get(tk.SEL_FIRST, tk.SEL_LAST)  # Получаем выделенный текст
        result_window.clipboard_clear()  # Очищаем буфер обмена
        result_window.clipboard_append(selected_text)  # Добавляем выделенный текст в буфер
        messagebox.showinfo("Скопировано", "Выделенный текст скопирован в буфер обмена")

    # Кнопка для копирования выделенного текста
    copy_button = tk.Button(result_window, text="Копировать выделенный текст", command=copy_to_clipboard)
    copy_button.pack(pady=5)

    # Кнопка для закрытия окна
    close_button = tk.Button(result_window, text="Закрыть", command=result_window.destroy)
    close_button.pack(pady=5)


# Создание простого UI с помощью tkinter
def create_ui():
    root = tk.Tk()
    root.title("Поиск в Excel файле")

    # Кнопка для выбора файла
    select_button = tk.Button(root, text="Выбрать файл", command=select_file)
    select_button.pack(pady=10)

    # Кнопка для поиска
    search_button = tk.Button(root, text="Поиск", command=search_in_file)
    search_button.pack(pady=10)

    # Запуск приложения
    root.mainloop()


# Запуск интерфейса
if __name__ == "__main__":
    create_ui()
