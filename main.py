from tkinter import *
import hh

root = Tk()
root.title("Auto_HH.RU")
root.geometry("270x240+650+250")


def show_number():
    num = batton_number_vvod.get()
    hh.logic_start(num)

# номер телефона
batton_number = Button(text="Номер телефона", background='#90EE90', font='Times 12', command=show_number)
batton_number.place(relx=0, rely=0.1, height=50, width=130, )

batton_number_vvod = Entry(background='#90EE90', font='Times 14')
batton_number_vvod.place(relx=0.5, rely=0.1, height=50, width=135)

# код который приходит на телефон
batton_kod = Button(text="Код", background='#90EE90', font='Times 12')
batton_kod.place(relx=0, rely=0.32, height=50, width=130, )

batton_number_kod = Entry(background='#90EE90', font='Times 14')
batton_number_kod.place(relx=0.5, rely=0.32, height=50, width=135)

# поле ввода вакансии
entry = Entry(background='#90EE90')
entry.place(anchor=N, relx=0.5, rely=0.65, height=30, width=260)

batton = Button(text="Откликаться на вакансии", background='#90EE90', font='Times 14')
batton.place(anchor=N, relx=0.5, rely=0.8, height=50, width=300, )

# пометка
text = Label(text="Введите название вакансии")
text.place(relx=-0.07, rely=0.58, height=10, width=300)

root.mainloop()
