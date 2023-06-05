from tkinter import *
import hh

root = Tk()
root.geometry("270x240+650+250")


def start():
    name_vacansion = entry.get()
    number_or_email = entry.get()

    hh.logic_start()


# текст вверху
textsp1 = Label(text="Введите название вакансии:", foreground="green")
textsp1.place(anchor=N, relx=0.5, rely=0, height=30, width=300)
# поле ввода вакансии
entry = Entry(background='#90EE90')
entry.place(anchor=N, relx=0.5, rely=0.1, height=30, width=230)

# текст вверху
textsp2 = Label(text="Введите номер или Email:", foreground="green")
textsp2.place(anchor=N, relx=0.5, rely=0.2, height=30, width=300)
# поле ввода вакансии
entry = Entry(background='#90EE90')
entry.place(anchor=N, relx=0.5, rely=0.3, height=30, width=230)

# кнопка поиска вакансий
batton = Button(text="Откликаться на вакансии", background='#90EE90', command=start)
batton.place(anchor=N, relx=0.5, rely=0.8, height=50, width=300, )

root.mainloop()
