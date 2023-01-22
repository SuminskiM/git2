def przywitanie(imie, nazwisko, wiek):
    print('Cześć', imie)
    if wiek >= 18:
        print('Szanowny', nazwisko)

dict = {'imie' : 'Kamil', 'nazwisko' : 'Kowalski'}
x = input('Podaj imię, nazwisko i wiek - oddziel spacją ').split()

przywitanie(x[0], x[1], int(x[2]))
przywitanie(dict['imie'], dict['nazwisko'], 22)


x = 0
while x < 5:
    print('Jakaś akcja')
    x += 1




# np. logowanie

PIN = '1234'
while True:
    y = input('Wprowadź kod PIN ')
    if y == PIN:
        przywitanie()
        break
print('Kod PIN prawidłowy.')
print('Czekaj na dalsze instrukcje.')
