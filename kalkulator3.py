import math
DZIALANIA = 7

a = float(input('Wpisz pierwsza liczbe '))
b = float(input('Wpisz druga liczbe '))

while DZIALANIA >= 7:

    DZIALANIA = int(input('Wybierz dzialanie: 0 - Dodawanie | 1 - Odejmowanie | 2 - Mnozenie | 3 - Dzielenie | 4 - Potegowanie | 5 - Logarytm naturalny | 6 - Pierwiastek kwadratowy '))

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

if DZIALANIA == 4:

    c = a ** b
    print('Wynik potegowania to: %f' % c)

if DZIALANIA == 5:

    c = math.log( a )
    print('Wynik to: %f' % c)

if DZIALANIA == 6:

    c = math.sqrt( a )
    print('Wynik to %f' % c)

if DZIALANIA == 7:
    
    
