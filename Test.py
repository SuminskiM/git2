def Przywitanie():
    print('Witaj')


PIN = '1234'
while True:
    x = input('Wprowadź kod PIN ')
    if x == PIN:
        Przywitanie()
        break
print('Kod PIN prawidłowy.')
print('Trwa pobieranie danych z bazy.')