print("Hello! Type the CPF number:")
search = input()

print("Searching...")
file = open("teste.txt","r") 
for line in file.readlines():
    if (search in line):
        print("Great! We have found your search!")
        break