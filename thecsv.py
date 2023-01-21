path = 'C://Users//vdi-student//Desktop//git2/rozliczenie.csv'
mode = 'r'
with open (path, mode) as plik_csv:
    content = plik_csv.readlines()
print(type(content))
print(len(content))
print(content)
print(content[4])

for i in range(len(content)):
    content[i] = content[i].split(';')
print(content)
print(content[5])
print(content[5][3])

dane = 'mama.tata.pies'
print(dane)
dane = dane.split('.')
print(dane)