from tkinter import *

root = Tk()
root.geometry("270x240+650+250")

#текст вверху
textsp1 = Label(text ="Введите название вакансии:", foreground="green")
textsp1.place(anchor=N, relx=0.5,rely=0,height=30, width=300)


#поле ввода
entry = Entry(background= '#90EE90')
entry.place(anchor=N,relx=0.5,rely=0.1, height=30, width=230)



#кнопка поиска вакансий
batton = Button(text ="Откликаться на вакансии", background='#90EE90')
batton.place(anchor=N,relx=0.5,rely=0.8, height=50, width=300, )

root.mainloop()
