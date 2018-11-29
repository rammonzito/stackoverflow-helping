#usando método
def somar():
    limite = 11
    total = 0
    for i in range(0, limite, 2):
        total += i  
    return total
total = somar()

print(total)

#simples
print(sum(range(0,181,2)))

