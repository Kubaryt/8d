import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QGridLaylout
app = QApplication(sys.argv)

class Calculator(QMainWindow)

    def __createbuttons(self):
        self.buttons{}
        buttonslaylout = QGridLaylout
        buttons = {'1': (0,0),
                   '2': (0,1),
                   '3': (0,2),
                   '+': (0,3),
                   '4': (1,0),
                   '5': (1,1),
                   '6': (1,2),
                   '-': (1,3),
                   '7': (2,0),
                   '8': (2,1),
                   '9': (2,2),
                   '*': (2,3),
                   '0': (3,1),
                   '=': (3,2),
                   '/': (3,3),
                  }
        
        def __createText(self):
            self.
        
        
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


def main():
    pycalc = QApplication(sys.argv)
    view = PyCalcUi()
    view.show()
    sys.exit(pycalc.exec_()
