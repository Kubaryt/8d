print('Wyodrebnianie cyfr z liczby dodatniej')

cyfr = int(input('Wprowadz ilosc cyfr '))
liczba = str(input('Wprowadz liczbe do wyodrebnienia '))
i = cyfr
r = 1
k = 0

while i >= 1:
    print('%d cyfra to: %s' % (r, liczba[k]))
    i = i - 1
    r = r + 1
    k = k + 1
