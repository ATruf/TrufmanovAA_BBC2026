from tkinter import *
from tkinter import messagebox
from tkinter import ttk

# банковское приложение


okno = Tk() # главное окно
okno.title("bank")
okno.geometry("500x560")

balance = 10000
n = 0 # счетчик операций


def knopka():
    global balance
    global n
    imya = e1.get()
    schet = e2.get()
    summa = e3.get()
    # print(imya, schet, summa)
    if imya == "":
        messagebox.showerror("Error", "Введите имя!!")
    else:
        if len(imya.split()) < 2:
            messagebox.showerror("Error", "Введите фио нормально")
        else:
            if len(schet) != 10:
                messagebox.showerror("Error", "Счет должен быть 10 цифр")
            else:
                if schet.isdigit() == False:
                    messagebox.showerror("Error", "Счет -это цифры")
                else:
                    try:
                        summa = float(summa.replace(",", "."))
                    except:
                        messagebox.showerror("Error", "Сумма- это не число")
                        return
                    if summa <= 0:
                        messagebox.showerror("Error", "Сумма больше 0")
                    else:
                        op = combo.get()
                        if op != "Пополнение" and summa > balance:
                            messagebox.showerror("Error", "Не хватает денег")
                        else:
                            vopros = messagebox.askyesno("Подтверждение", op + " " + str(summa) + "?")
                            if vopros == True:
                                if op == "Пополнение":
                                    balance = balance + summa
                                else:
                                    balance = balance - summa
                                n = n + 1
                                if sms.get() == 1:
                                    s = "da"
                                else:
                                    s = "net"
                                text = "#" + str(n) + " " + imya + " " + schet + " " + op + " " + str(summa) + " " + valuta.get() + " sms:" + s + " balance:" + str(balance)
                                print(text) # в консоль
                                rez.config(state=NORMAL)
                                rez.insert(END, text + "\n")
                                rez.config(state=DISABLED)
                                l2.config(text="Баланс: " + str(balance))
                                e3.delete(0, END)
                                messagebox.showinfo("ok", "Готово")


def ochistit():
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
def vyhod():
    if messagebox.askokcancel("Выход", "Точно выйти?") == True:
        okno.destroy()
def smena(event):
    # print("smena")
    l2.config(text="Баланс: " + str(balance) + " (" + combo.get() + ")")
def enter(event):
    knopka()


# текст
l1 = Label(okno, text="БАНК", font=("Arial", 20))
l1.grid(row=0, column=0, columnspan=2, pady=10)
l2 = Label(okno, text="Баланс: " + str(balance))
l2.grid(row=1, column=0, columnspan=2)

# поля ввода
Label(okno, text="ФИО").grid(row=2, column=0, pady=5)
e1 = Entry(okno, width=30)
e1.grid(row=2, column=1)
Label(okno, text="Счет").grid(row=3, column=0, pady=5)
e2 = Entry(okno, width=30)
e2.grid(row=3, column=1)
Label(okno, text="Сумма").grid(row=4, column=0, pady=5)
e3 = Entry(okno, width=30)
e3.grid(row=4, column=1)

# выбор параметров
Label(okno, text="Операция").grid(row=5, column=0, pady=5)
combo = ttk.Combobox(okno, values=["Пополнение", "Снятие", "Перевод"], state="readonly", width=27)
combo.current(0)
combo.grid(row=5, column=1)
combo.bind("<<ComboboxSelected>>", smena)

valuta = StringVar()
valuta.set("RUB")
Label(okno, text="Валюта").grid(row=6, column=0)
r1 = Radiobutton(okno, text="RUB", variable=valuta, value="RUB")
r1.grid(row=6, column=1, sticky="w")
r2 = Radiobutton(okno, text="USD", variable=valuta, value="USD")
r2.grid(row=7, column=1, sticky="w")
r3 = Radiobutton(okno, text="EUR", variable=valuta, value="EUR")
r3.grid(row=8, column=1, sticky="w")

sms = IntVar()
sms.set(1)
c1 = Checkbutton(okno, text="SMS", variable=sms)
c1.grid(row=9, column=1, sticky="w")

# кнопки
b1 = Button(okno, text="Выполнить", command=knopka)
b1.grid(row=10, column=0, pady=10)
b2 = Button(okno, text="Очистить", command=ochistit)
b2.grid(row=10, column=1)
b3 = Button(okno, text="Выход", command=vyhod)
b3.grid(row=11, column=0, columnspan=2)

# сюда выводятся результаты
rez = Text(okno, height=8, width=58, state=DISABLED)
rez.grid(row=12, column=0, columnspan=2, pady=10)

okno.bind("<Return>", enter)
okno.bind("<Escape>", lambda e: vyhod())

okno.mainloop()