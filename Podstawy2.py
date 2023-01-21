import os

print(os.getcwd())
os.chdir('C:\\Users\\vdi-student\\Desktop')
print(os.getcwd())
os.mkdir('new_folder')
os.rename('new_folder', 'new_folder2')
os.mkdir('new_folder2')