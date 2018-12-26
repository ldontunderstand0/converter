import sys
import math
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QPushButton, QComboBox, QApplication)


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.lbl = QLabel("", self)
        self.combo = QComboBox(self)
        self.combo.addItems(["Длина", "Масса", "Температура", "Площадь", "Скорость", "Объём", "Время", "Сила"])
        self.combo.addItems(["Скорость вращения", "Угловая мера", "Объём данных"])
        self.combo.move(30, 40)

        self.massa = ['- тонна', '- килограмм', '- грамм', '- миллиграмм']
        self.dlina = ['- километр', '- метр', '- сантиметр', '- миллиметр']
        self.tem = ['- градус Цельсия', '- градус Кельвина', '- градус Фаренгейта', '- градус Реомюра']
        self.plo = ['- гектар', '- ар', '- квадратный метр', '- квадратный сантиметр']
        self.speed = ['- метр в секунду', '- километр в час', '- метр в минуту', '- километр в минуту']
        self.obiom = ['- кубический метр', '- кубический сантиметр', '- литр', '- миллилитр']
        self.vremia = ['- сутки', '- час', '- минута', '- секунда']
        self.sila = ['- меганьютон', '- килоньютон', '- ньютон', '- миллиньютон']
        self.ygl = ['- радиан', '- градус', '- минута', '- секунда']
        self.dan = ['- килобайт', '- байт', '- килобит', '- бит']
        self.speedvr = ['- Оборот в сутки', '- Оборот в час', '- Оборот в минуту', '- Оборот в секунду']

        self.edit1 = QLineEdit(self)
        self.edit1.resize(130, 20)
        self.edit1.move(160, 95)

        self.edit2 = QLineEdit(self)
        self.edit2.resize(130, 20)
        self.edit2.move(160, 121)

        self.edit3 = QLineEdit(self)
        self.edit3.resize(130, 20)
        self.edit3.move(160, 147)

        self.edit4 = QLineEdit(self)
        self.edit4.resize(130, 20)
        self.edit4.move(160, 173)

        btn = QPushButton('Посчитать', self)
        btn.resize(130, 30)
        btn.move(30, 205)
        btn.clicked.connect(self.run)

        btn2 = QPushButton('Очистить', self)
        btn2.resize(130, 30)
        btn2.move(160, 205)
        btn2.clicked.connect(self.clear)

        self.er = QLabel(self)
        self.er.resize(200, 30)
        self.er.move(50, 235)

        self.lbl.resize(130, 100)
        self.lbl.move(30, 100)
        self.combo.activated[str].connect(self.onActivated)

        self.lbl1 = QLabel("Выберете нужное измерение:", self)
        self.lbl2 = QLabel("Укажите величины и нажмите 'посчитать'", self)
        self.lbl1.move(30, 20)
        self.lbl2.move(30 ,70)

        self.tx = ''
        self.name = ''
        self.p = math.pi

        self.setGeometry(300, 300, 320, 270)
        self.setWindowTitle('Конвертер')
        self.show()

    def clear(self):
        self.edit1.setText('')
        self.edit2.setText('')
        self.edit3.setText('')
        self.edit4.setText('')

    def run(self):
        try:
            self.er.setText('')
            r = [0, 0, 0, 0]
            if self.name == 'Масса':
                tonna = 0
                kg = 0
                g = 0
                mg = 0
                z = 0
                if self.edit1.text() != '':
                    tonna = float(self.edit1.text())
                    z = 1
                if self.edit2.text() != '':
                    kg = float(self.edit2.text())
                    z = 2
                if self.edit3.text() != '':
                    g = float(self.edit3.text())
                    z = 3
                if self.edit4.text() != '':
                    mg = float(self.edit4.text())
                    z = 4
                if z == 1:
                    kg = tonna * 1000
                    g = tonna * 1000000
                    mg = tonna * 1000000000
                elif z == 2:
                    tonna = kg * 0.001
                    g = kg * 1000
                    mg = kg * 1000000
                elif z == 3:
                    tonna = g * 0.000001
                    kg = g * 0.001
                    mg = g * 1000
                elif z == 4:
                    tonna = mg * 0.000000001
                    kg = mg * 0.000001
                    g = mg * 0.001
                r = [tonna, kg, g, mg]
            elif self.name == 'Длина':
                km = 0
                m = 0
                sm = 0
                mm = 0
                z = 0
                if self.edit1.text() != '':
                    km = float(self.edit1.text())
                    z = 1
                if self.edit2.text() != '':
                    m = float(self.edit2.text())
                    z = 2
                if self.edit3.text() != '':
                    sm = float(self.edit3.text())
                    z = 3
                if self.edit4.text() != '':
                    mm = float(self.edit4.text())
                    z = 4
                if z == 1:
                    m = km * 1000
                    sm = km * 100000
                    mm = km * 1000000
                elif z == 2:
                    km = m * 0.001
                    sm = m * 100
                    mm = m * 1000
                elif z == 3:
                    km = sm * 0.00001
                    m = sm * 0.01
                    mm = sm * 10
                elif z == 4:
                    km = mm * 0.000001
                    m = mm * 0.001
                    sm = mm * 0.1
                r = [km, m, sm, mm]
            elif self.name == 'Объём':
                m = 0
                sm = 0
                l = 0
                ml = 0
                z = 0
                if self.edit1.text() != '':
                    m = float(self.edit1.text())
                    z = 1
                if self.edit2.text() != '':
                    sm = float(self.edit2.text())
                    z = 2
                if self.edit3.text() != '':
                    l = float(self.edit3.text())
                    z = 3
                if self.edit4.text() != '':
                    ml = float(self.edit4.text())
                    z = 4
                if z == 1:
                    sm = m * 1000000
                    l = m * 1000
                    ml = m * 1000000
                elif z == 2:
                    m = sm * 0.000001
                    l = sm * 0.001
                    ml = sm * 1
                elif z == 3:
                    m = l * 0.001
                    sm = l * 1000
                    ml = l * 1000
                elif z == 4:
                    m = ml * 0.000001
                    sm = ml * 1
                    l = ml * 0.001
                r = [m, sm, l, ml]
            elif self.name == 'Температура':
                cel = 0
                kel = 0
                far = 0
                reo = 0
                z = 0
                if self.edit1.text() != '':
                    cel = float(self.edit1.text())
                    z = 1
                if self.edit2.text() != '':
                    kel = float(self.edit2.text())
                    z = 2
                if self.edit3.text() != '':
                    far = float(self.edit3.text())
                    z = 3
                if self.edit4.text() != '':
                    reo = float(self.edit4.text())
                    z = 4
                if z == 1:
                    kel = cel + 273.15
                    far = (cel * 1.8) + 32
                    reo = cel * 0.8
                elif z == 2:
                    cel = kel - 273.15
                    far = ((9 * (kel - 273.15)) / 5) + 32
                    reo = (kel - 273.15) * 0.8
                elif z == 3:
                    cel = ((far - 32) * 5) / 9
                    kel = ((5 * (far - 32)) / 9) + 273.15
                    reo = ((far - 32) * 4) / 9
                elif z == 4:
                    cel = (reo * 5) / 4
                    kel = (1.25 * reo) + 273.15
                    far = (reo * 9) / 4 + 32
                r = [cel, kel, far, reo]
            elif self.name == 'Площадь':
                ga = 0
                ar = 0
                m = 0
                sm = 0
                z = 0
                if self.edit1.text() != '':
                    ga = float(self.edit1.text())
                    z = 1
                if self.edit2.text() != '':
                    ar = float(self.edit2.text())
                    z = 2
                if self.edit3.text() != '':
                    m = float(self.edit3.text())
                    z = 3
                if self.edit4.text() != '':
                    sm = float(self.edit4.text())
                    z = 4
                if z == 1:
                    ar = ga * 100
                    m = ga * 10000
                    sm = ga * 100000000
                elif z == 2:
                    ga = ar * 0.01
                    m = ar * 100
                    sm = ar * 1000000
                elif z == 3:
                    ga = m * 0.0001
                    ar = m * 0.01
                    sm = m * 10000
                elif z == 4:
                    ga = sm * 0.00000001
                    ar = sm * 0.000001
                    m = sm * 0.0001
                r = [ga, ar, m, sm]
            elif self.name == 'Скорость':
                m_s = 0
                k_c = 0
                m_m = 0
                k_m = 0
                z = 0
                if self.edit1.text() != '':
                    m_s = float(self.edit1.text())
                    z = 1
                if self.edit2.text() != '':
                    k_c = float(self.edit2.text())
                    z = 2
                if self.edit3.text() != '':
                    m_m = float(self.edit3.text())
                    z = 3
                if self.edit4.text() != '':
                    k_m = float(self.edit4.text())
                    z = 4
                if z == 1:
                    k_c = m_s * 3.6
                    m_m = m_s * 60
                    k_m = m_s * 0.06
                elif z == 2:
                    m_s = k_c / 3.6
                    m_m = k_c / 0.06
                    k_m = k_c / 60
                elif z == 3:
                    m_s = m_m / 60
                    k_c = m_m * 0.06
                    k_m = m_m * 0.001
                elif z == 4:
                    m_s = k_m / 0.06
                    k_c = k_m * 60
                    m_m = k_m * 1000
                r = [m_s, k_c, m_m, k_m]
            elif self.name == 'Время':
                sut = 0
                ch = 0
                m = 0
                sec = 0
                z = 0
                if self.edit1.text() != '':
                    sut = float(self.edit1.text())
                    z = 1
                if self.edit2.text() != '':
                    ch = float(self.edit2.text())
                    z = 2
                if self.edit3.text() != '':
                    m = float(self.edit3.text())
                    z = 3
                if self.edit4.text() != '':
                    sec = float(self.edit4.text())
                    z = 4
                if z == 1:
                    ch = sut * 24
                    m = sut * 1440
                    sec = sut * 86400
                elif z == 2:
                    sut = ch / 24
                    m = ch * 60
                    sec = ch * 3600
                elif z == 3:
                    sut = m / (60 * 24)
                    ch = m / 60
                    sec = m * 60
                elif z == 4:
                    sut = sec / (24 * 60 * 60)
                    ch = sec / (60 * 60)
                    m = sec / 60
                r = [sut, ch, m, sec]
            elif self.name == 'Сила':
                Mn = 0
                kn = 0
                n = 0
                mn = 0
                z = 0
                if self.edit1.text() != '':
                    Mn = float(self.edit1.text())
                    z = 1
                if self.edit2.text() != '':
                    kn = float(self.edit2.text())
                    z = 2
                if self.edit3.text() != '':
                    n = float(self.edit3.text())
                    z = 3
                if self.edit4.text() != '':
                    mn = float(self.edit4.text())
                    z = 4
                if z == 1:
                    kn = Mn * 1000
                    n = Mn * 1000000
                    mn = Mn * 1000000000
                elif z == 2:
                    Mn = kn / 1000
                    n = kn * 1000
                    mn = kn * 1000000
                elif z == 3:
                    Mn = n / 1000000
                    kn = n / 1000
                    mn = n * 1000
                elif z == 4:
                    Mn = mn / 1000000000
                    kn = mn / 1000000
                    n = mn / 1000
                r = [Mn, kn, n, mn]
            elif self.name == 'Угловая мера':
                r = 0
                g = 0
                m = 0
                s = 0
                z = 0
                if self.edit1.text() != '':
                    r = float(self.edit1.text())
                    z = 1
                if self.edit2.text() != '':
                    g = float(self.edit2.text())
                    z = 2
                if self.edit3.text() != '':
                    m = float(self.edit3.text())
                    z = 3
                if self.edit4.text() != '':
                    s = float(self.edit4.text())
                    z = 4
                if z == 1:
                    g = (180 / self.p) * r
                    m = g * 60
                    s = g * 3600
                elif z == 2:
                    r = self.p / (180 / g)
                    m = g * 60
                    s = g * 3600
                elif z == 3:
                    g = m / 60
                    s = m * 60
                    r = self.p / (180 / g)
                elif z == 4:
                    g = s / 3600
                    m = s / 60
                    r = self.p / (180 / g)
                r = [r, g, m, s]
            elif self.name == 'Объём данных':
                kbait = 0
                bait = 0
                kbit = 0
                bit = 0
                z = 0
                if self.edit1.text() != '':
                    kbait = float(self.edit1.text())
                    z = 1
                if self.edit2.text() != '':
                    bait = float(self.edit2.text())
                    z = 2
                if self.edit3.text() != '':
                    kbit = float(self.edit3.text())
                    z = 3
                if self.edit4.text() != '':
                    bit = float(self.edit4.text())
                    z = 4
                if z == 1:
                    bait = kbait * 1024
                    kbit = kbait * 8
                    bit = kbait * 8192
                elif z == 2:
                    kbait = bait / 1024
                    kbit = kbait * 8
                    bit = bait * 8
                elif z == 3:
                    kbait = kbit / 8
                    bait = kbait * 1024
                    bit = kbit * 1024
                elif z == 4:
                    kbit = bit / 1024
                    bait = bit / 8
                    kbait = bait / 1024
                r = [kbait, bait, kbit, bit]
            elif self.name == 'Скорость вращения':
                sut = 0
                ch = 0
                m = 0
                sec = 0
                z = 0
                if self.edit1.text() != '':
                    sut = float(self.edit1.text())
                    z = 1
                if self.edit2.text() != '':
                    ch = float(self.edit2.text())
                    z = 2
                if self.edit3.text() != '':
                    m = float(self.edit3.text())
                    z = 3
                if self.edit4.text() != '':
                    sec = float(self.edit4.text())
                    z = 4
                if z == 1:
                    ch = sut / 24
                    m = sut / 1440
                    sec = sut / 86400
                elif z == 2:
                    sut = ch * 24
                    m = ch / 60
                    sec = ch / 3600
                elif z == 3:
                    sut = m * (60 * 24)
                    ch = m * 60
                    sec = m / 60
                elif z == 4:
                    sut = sec * (24 * 60 * 60)
                    ch = sec * (60 * 60)
                    m = sec * 60
                r = [sut, ch, m, sec]
            for i in range(4):
                if r[i] == int(r[i]):
                    r[i] = int(r[i])
            self.edit1.setText(str(r[0]))
            self.edit2.setText(str(r[1]))
            self.edit3.setText(str(r[2]))
            self.edit4.setText(str(r[3]))
        except ValueError:
            self.er.setText('Внимание! Необходимо вводить числа!')

    def onActivated(self, text):
        self.name = text
        tx = ''
        t = []
        if text == "Масса":
            t = self.massa
        if text == "Длина":
            t = self.dlina
        if text == "Температура":
            t = self.tem
        if text == "Объём":
            t = self.obiom
        if text == "Площадь":
            t = self.plo
        if text == "Скорость":
            t = self.speed
        if text == "Время":
            t = self.vremia
        if text == "Сила":
            t = self.sila
        if text == "Угловая мера":
            t = self.ygl
        if text == "Объём данных":
            t = self.dan
        if text == "Скорость вращения":
            t =self.speedvr
        for i in range(4):
            tx += t[i] + '\n\n'
        self.lbl.setText(tx)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
