path = 'C://Users//vdi-student//Desktop//Maciej//git2/rozliczenie.csv'
mode = 'r'
with open (path, mode) as plik_csv:
    content = plik_csv.readlines()
for i in range(len(content)):
    content[i] = content[i].replace('\n','')
    content[i] = content[i].split(';')

2# Obliczanie średniej wypłaty.
total = 0
for i in range(1, len(content)):
    total = total + int(content[i][1])
average = total/(len(content)-1)
print('Średnia wypłata wynosi' ,round(average, 2),'złotych.')

# Obliczanie liczby kobiet na urlopie macierzyńskim.
totalm = 0
for i in range(1, len(content)):
    if content[i][4] == 't' and content[i][3] == 'k':
        totalm += 1
print(totalm)
