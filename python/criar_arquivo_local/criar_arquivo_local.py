try:
    nome = input('Digite o nome do arquivo: ')
    #aqui voce vai verificar se o arquivo existe
    arquivo = open(nome, 'r+')
except FileNotFoundError:
    arquivo = open(nome, 'w+')
    arquivo.writelines(u'Conteudo arquivo...')
#aqui você pode continuar o desenvolvimento
arquivo.close()
