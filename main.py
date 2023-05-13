import tkinter as tk

import ttkbootstrap as ttk


# функция для кнопки
def confirm_func():
    km = entry_var.get()
    output_var.set(str(1.61 * km))


# Конфигурация приложения
app = ttk.Window(themename='journal')
app.title('My application')
app.geometry('300x150')

# Заголовок
main_label = ttk.Label(master=app, text='Мили в километры', font='TimesNewRoman 24 bold')
main_label.pack()

# контейнер ввода
entry_space_container = ttk.Frame(master=app)
entry_space_container.pack()

# поле ввода
entry_var = ttk.IntVar()
entry_frame = ttk.Entry(master=entry_space_container, textvariable=entry_var)
entry_frame.pack(side='left')

# кнопка ввода
confirm_button = ttk.Button(master=entry_space_container, text=('подтвердить'), command=confirm_func)
confirm_button.pack(side='right')

# вывод результата работы алгоритма на экран
output_var = ttk.StringVar()
output_label = ttk.Label(master=app, text='Здесь будет вывод', font='TimesNewRoman 16', textvariable=output_var)
output_label.pack()



app.mainloop()
