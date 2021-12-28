import math
'''
import QtQuick 2.3
import QtQuick.Controls 1.4
'''
'''
import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget
app = QApplication(sys.argv)
'''

loop = 1

def Dzialania():
    DZIALANIA = 8


    #WYBOR DZIALANIA

    while DZIALANIA >= 8:
    
        DZIALANIA = int(input('Wybierz dzialanie: 0 - Dodawanie | 1 - Odejmowanie | 2 - Mnozenie | 3 - Dzielenie | 4 - Potegowanie | 5 - Logarytm naturalny | 6 - Pierwiastek kwadratowy | 7 - Średnia arytmetyczna '))


    #WPROWADZANIE LICZB (0-4)

    if DZIALANIA <= 3:

        a = float(input('Wprowadz pierwsza liczbe '))
        b = float(input('Wprowadz druga liczbe '))


    #DZIALANIA (0-4)

    if DZIALANIA == 0:

        c = a + b

    if DZIALANIA == 1:

        c = a - b

    if DZIALANIA == 2:

        c = a * b
    
    if DZIALANIA == 3:

        while b == 0:

            b = float(input('Wprowadz druga liczbe '))

        c = a / b

    if DZIALANIA == 4:

        c = a ** b        

    #WPROWADZANIE LICZBY (5-6)

    if DZIALANIA >= 5 and DZIALANIA != 7:

        a = float(input('Wprowadz pierwsza liczbe '))


    #DZIALANIA (5-6)


    if DZIALANIA == 5:

        math.log( a )

    if DZIALANIA == 6:
    
        math.sqrt( a )

    #SREDNIA ARYTMETYCZNA

    if DZIALANIA == 7:

        b = 0
        while b == 0:

            b = int(input('Wprowadz ilosc liczb '))
    
        i = b
        r = 1
        wynik = 0

        while i >= 1:

            a = float(input('Wprowadz liczbe po raz %g ' % r))
            wynik = wynik + a
            r = r + 1
            i = i - 1
    
        c = wynik / b
    
    return c

while loop:

    c = Dzialania()

    #WYSWIETLANIE WYNIKU
    '''
    window = QWidget()
    window.setWindowTitle('PyQt5 App')
    window.setGeometry(150, 150, 330, 130)
    window.move(60, 15)
    WynikMsg = QLabel('<h1>Wynik to: %f</h1>' % c, parent=window)
    WynikMsg.move(30, 50)
    window.show()
    sys.exit(app.exec_())
    '''

    print('Wynik to: %f' %  c)

    #POWTARZANIE

    loop = int(input('Aby zakończyć powtarzanie kodu wpisz 0: '))
