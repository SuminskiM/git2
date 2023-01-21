path = 'C://Users//vdi-student//Desktop//git2/rozliczenie.csv'
mode = 'r'
with open (path, mode) as plik_csv:
    content = plik_csv.readlines()

print(content)