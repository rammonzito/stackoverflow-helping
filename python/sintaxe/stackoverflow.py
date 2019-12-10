import os
def painel():
    print('1 - inserir outro nome\n2 - contar nome\n3 - remover o último nome\n4 - inserir nome em índice específico')
    print('5 - remover nome específico\n6 - remover o último nome\n7 - remover a primeira ocorrência do nome')
    print('8 - retornar índice de nome específico\n9 - reverter toda a lista\n10 - verifica se há o nome da lista')
    print('11 - mostrar lista\n12 - sair da programa')
    a = int(input('Digite o que deseja fazer com a lista: '))

clear = lambda: os.system('clear') #para limpar o console durante a execução da programa
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
lista = [ ] #declarando lista dinâmica 'infinita'
i = 0
while True: #loop infinito
    a = input(f'Digite o nome de índice {i}: ') #toda input sem cast retorna uma string
    if a in lista:
        print('Esse nome já consta na lista.')
        e = input('\nDeseja continuar (sim ou nao)? ')
    else:
        i += 1 #incremento de +1 em i
        lista.append(a)
        e = input('\nDeseja continuar (sim ou nao)? ')
        if e == 'sim':
            break
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
while True:    
    painel()
    if a == '1':
        clear() #limpar o terminal
        a = input('Digite o novo nome: ')
        if a in lista:
            print('Este nome já consta na lista.')
        else:
            lista.append(a)    
    elif a == '2':
        clear() 
        a = input('Digite o nome que deseja contar: ')
        print(f'\nHá {lista.count()} de {a} na lista.')
    elif a == '3':
        clear()
        a = input('Digite o nome que deseja remover: ')
        if a in lista:
            lista.pop()
            print('Nome removido com sucesso.')
        else:
            print('Nome não consta na lista.')
    elif a == '4':
        clear()
        a = input("Digite o nome: ")
        i = int(input('Digite o índice onde deseja inserir: '))
        if a in lista:
            print('Nome já consta na lista.')
        else:
            lista.insert(a, i)
    elif a == '5':
        clear()
        a = input('Digite o nome que deseja remover: ')
        if a in lista:
            lista.pop(lista.index(a))
            print('Nome removido com sucesso.')
        else:
            print('Nome não consta na lista.')
    elif a == '6':
        clear()
        if lista == []:
            print('Lista vazia.')
        else:
            lista.append()
            print('Nome removido com sucesso.')
    elif a == '7':
        clear()
        a = input('Digite o nome: ')
        if a in lista:
            lista.remove(a)
            print('Nome removido com sucesso.')
        else:
            print('Nome não consta da lista')
    elif a == '8':
        clear()
        a = input('Digite o nome para retorno de índice: ')
        if nome in lista:            
            print(f'O nome se encontra no índice {lista.index(a)}.')
        else:
            print('Nome não consta na lista.')
    elif a == '9':
        clear()

    elif a == '10':
        clear()
        lista.reverse()
        print('Lista invertida com sucesso.')
    elif a == '11':
        clear()
        print(lista)
    elif a == '12':
        clear()
        print('Programa finalizado')
        break
    else:
        print('Digite uma das opções acima: ', end = '')