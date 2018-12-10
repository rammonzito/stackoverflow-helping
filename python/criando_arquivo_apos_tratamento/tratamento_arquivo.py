import string

def ReadFile():
    global data #ajuste
    f=open("chap.1_esp.txt",'r')
    data = f.read()
    while True:
        line=f.readline()        
        if not line:
            break
        data.append(line)

    f.close()
    for i in range(len(data)):
        print(data[i],end=" ")

def PunctuationLowercase():
    global dataLower #ajuste
    global dataPunctuation #ajuste
    dataLower = []
    dataPunctuation = []
    translator=str.maketrans('','', string.punctuation)
    for i in range(len(data)):
        dataLower.append(data[i].lower())   
        dataPunctuation.append(dataLower[i].translate(translator)) 
        print(dataPunctuation[i],end=" ") 

def SaveFile():
    texto="Isto é uma variável que vai ser guardada num ficheiro."
    with open("chap.1_new.txt","w") as f:
        f.write(texto)   
        f.write("Isto vai ser guardado num ficheiro.")
        for i in range(len(data)):
                dataPunctuation.append(dataLower[i]) #ajuste
                f.write(dataPunctuation[i]) #ajuste

    f.close()

if __name__ == "__main__":
    ReadFile()
    PunctuationLowercase()
    SaveFile()