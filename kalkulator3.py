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

while loop:

    DZIALANIA = 8


    #WYBOR DZIALANIA

    while DZIALANIA >= 8:
    
        DZIALANIA = int(input('Wybierz dzialanie: 0 - Dodawanie | 1 - Odejmowanie | 2 - Mnozenie | 3 - Dzielenie | 4 - Potegowanie | 5 - Logarytm naturalny | 6 - Pierwiastek kwadratowy | 7 - Średnia arytmetyczna '))


    #WPROWADZANIE LICZB (0-3)

    if DZIALANIA <= 3:

        a = float(input('Wprowadz pierwsza liczbe '))
        b = float(input('Wprowadz druga liczbe '))


    #WYPROWADZANIE WYNIKU (0-3)

    if DZIALANIA == 0:

        c = a + b
        print('Wynik dodawania to: %f' %  c )

    if DZIALANIA == 1:

        c = a - b
        print('Wynik odejmowania to: %f' %  c )

    if DZIALANIA == 2:

        c = a * b
        print('Wynik mnozenia to: %f' %  c )
    
    if DZIALANIA == 3:

        while b == 0:
    
            b = float(input('Wpisz druga liczbe '))
    
        c = a / b
        print('Wynik dzielenia to: %f' % c )


    #WPROWADZANIE LICZBY (4-6)

    if DZIALANIA >= 4 and DZIALANIA != 7:

        a = float(input('Wprowadz pierwsza liczbe '))


    #WYPROWADZANIE WYNIKU (0-3)

    if DZIALANIA == 4:

        c = a ** b
        print('Wynik potegowania to: %f' % c)

    if DZIALANIA == 5:

        c = math.log( a )
        print('Wynik to: %f' % c)

    if DZIALANIA == 6:
    
        c = math.sqrt( a )
        print('Wynik to %f' % c)


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
        print('Wynik to: %f' % c)

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

    #POWTARZANIE

    loop = int(input('Aby zakończyć powtarzanie kodu wpisz 0: '))
