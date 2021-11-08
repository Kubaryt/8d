import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget
app = QApplication(sys.argv)

DZIALANIA = 4


#WYBOR DZIALANIA

while DZIALANIA >= 4:
    
    DZIALANIA = int(input('Wybierz dzialanie: 0 - Dodawanie | 1 - Odejmowanie | 2 - Mnozenie | 3 - Dzielenie '))



if DZIALANIA == 0:

    a = int(input('Wpisz pierwsza liczbe '))
    b = int(input('Wpisz druga liczbe '))
    c = a + b
    #print('Wynik dodawania to: %g' %  c )

if DZIALANIA == 1:

    a = int(input('Wpisz pierwsza liczbe '))
    b = int(input('Wpisz druga liczbe '))
    c = a - b
    #print('Wynik odejmowania to: %g' %  c )

if DZIALANIA == 2:

    a = int(input('Wpisz pierwsza liczbe '))
    b = int(input('Wpisz druga liczbe '))
    c = a * b
    #print('Wynik mnozenia to: %g' %  c )

if DZIALANIA == 3:

    a = int(input('Wpisz pierwsza liczbe '))
    b = 0

    while b == 0:

        b = int(input('Wpisz druga liczbe '))

    c = a / b
    #print('Wynik dzielenia to: %g' % c )


window = QWidget()
window.setWindowTitle('PyQt5 App')
window.setGeometry(150, 150, 330, 130)
window.move(60, 15)
WynikMsg = QLabel('<h1>Wynik to: %f</h1>' % c, parent=window)
WynikMsg.move(30, 50)
window.show()
sys.exit(app.exec_())
