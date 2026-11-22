import sys
from PyQt6.QtWidgets import *

# банк на qt

balance = 10000
n = 0


class Okno(QMainWindow): # главное окно
    def __init__(self):
        super().__init__()
        self.setWindowTitle("bank qt")
        self.resize(500, 560)

        w = QWidget()
        self.setCentralWidget(w)
        lay = QVBoxLayout()
        w.setLayout(lay)

        # текст
        self.l1 = QLabel("БАНК")
        lay.addWidget(self.l1)
        self.l2 = QLabel("Баланс: " + str(balance))
        lay.addWidget(self.l2)

        # поля ввода
        self.e1 = QLineEdit()
        self.e1.setPlaceholderText("ФИО")
        lay.addWidget(self.e1)
        self.e2 = QLineEdit()
        self.e2.setPlaceholderText("Счет")
        lay.addWidget(self.e2)
        self.e3 = QLineEdit()
        self.e3.setPlaceholderText("Сумма")
        lay.addWidget(self.e3)

        # выбор параметров
        self.combo = QComboBox()
        self.combo.addItem("Пополнение")
        self.combo.addItem("Снятие")
        self.combo.addItem("Перевод")
        lay.addWidget(self.combo)

        self.r1 = QRadioButton("RUB")
        self.r1.setChecked(True)
        self.r2 = QRadioButton("USD")
        self.r3 = QRadioButton("EUR")
        lay.addWidget(self.r1)
        lay.addWidget(self.r2)
        lay.addWidget(self.r3)

        self.c1 = QCheckBox("SMS")
        self.c1.setChecked(True)
        lay.addWidget(self.c1)

        # кнопки
        self.b1 = QPushButton("Выполнить")
        self.b2 = QPushButton("Очистить")
        self.b3 = QPushButton("Выход")
        lay.addWidget(self.b1)
        lay.addWidget(self.b2)
        lay.addWidget(self.b3)

        # сюда результаты
        self.rez = QTextEdit()
        self.rez.setReadOnly(True)
        lay.addWidget(self.rez)

        # события
        self.b1.clicked.connect(self.knopka)
        self.b2.clicked.connect(self.ochistit)
        self.b3.clicked.connect(self.close)
        self.e3.returnPressed.connect(self.knopka)
        self.combo.currentTextChanged.connect(self.smena)

    def smena(self):
        self.l2.setText("Баланс: " + str(balance) + " (" + self.combo.currentText() + ")")

    def ochistit(self):
        self.e1.setText("")
        self.e2.setText("")
        self.e3.setText("")

    def knopka(self):
        global balance
        global n
        imya = self.e1.text()
        schet = self.e2.text()
        summa = self.e3.text()
        # print(imya, schet, summa)
        if imya == "":
            QMessageBox.critical(self, "Error", "Введи имя!!")
        else:
            if len(imya.split()) < 2:
                QMessageBox.critical(self, "Error", "Введи фио нормально")
            else:
                if len(schet) != 10:
                    QMessageBox.critical(self, "Error", "Счет должен быть 10 цифр")
                else:
                    if schet.isdigit() == False:
                        QMessageBox.critical(self, "Error", "Счет это цифры")
                    else:
                        try:
                            summa = float(summa.replace(",", "."))
                        except:
                            QMessageBox.critical(self, "Error", "Сумма не число")
                            return
                        if summa <= 0:
                            QMessageBox.critical(self, "Error", "Сумма больше 0")
                        else:
                            op = self.combo.currentText()
                            if op != "Пополнение" and summa > balance:
                                QMessageBox.critical(self, "Error", "Не хватает денег")
                            else:
                                vopros = QMessageBox.question(self, "Подтверждение", op + " " + str(summa) + "?")
                                if vopros == QMessageBox.StandardButton.Yes:
                                    if op == "Пополнение":
                                        balance = balance + summa
                                    else:
                                        balance = balance - summa
                                    n = n + 1
                                    if self.c1.isChecked():
                                        s = "da"
                                    else:
                                        s = "net"
                                    if self.r1.isChecked():
                                        v = "RUB"
                                    elif self.r2.isChecked():
                                        v = "USD"
                                    else:
                                        v = "EUR"
                                    text = "#" + str(n) + " " + imya + " " + schet + " " + op + " " + str(summa) + " " + v + " sms:" + s + " balance:" + str(balance)
                                    print(text) # в консоль
                                    self.rez.append(text)
                                    self.l2.setText("Баланс: " + str(balance))
                                    self.e3.setText("")
                                    QMessageBox.information(self, "ok", "Готово")

    def closeEvent(self, event):
        o = QMessageBox.question(self, "Выход", "Точно выйти?")
        if o == QMessageBox.StandardButton.Yes:
            event.accept()
        else:
            event.ignore()


app = QApplication(sys.argv)
okno = Okno()
okno.show()
app.exec()