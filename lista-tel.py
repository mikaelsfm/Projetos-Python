lista_contatos= {
    'Mikael': ['12345678'],                                                 #contatos teste já inseridos na lista#
    'Luciana': ['87654321']
}

def menuPrincipal():
    while True:
        print('***Agenda Telefônica***')
        print('1 - Incluir Contato')                                        # Função para o menu principal  #
        print('2 - Incluir Telefone em um contato')
        print('3 - Excluir telefone de um contato')
        print('4 - Excluir Contato')
        print('5 - Consultar Lista')
        print('6 - Encerrar')
        opcao = int(input('Selecione uma opção: '))

        if opcao == 1:
            incluirNovoNome()
            print()
        elif opcao == 2:
            incluirTelefone()
            print()
        elif opcao == 3:
            excluirTelefone()
            print()
        elif opcao == 4:
            excluirNome()
            print()
        elif opcao == 5:
            consultarNome()
            print()
        elif opcao == 6:
            print('Encerrando programa! :)')
            break
        else:
            print('Opção inválida, selecione uma opção de 1 a 6')
            print()
#---------------------------------------------------------------------------------------------------------------------#
def incluirNovoNome():
    print()
    nome = input('Nome: ')                                                  # Função para incluir um contato #
    lista_contatos[nome] = []
    lista_contatos[nome].append(input('Telefone: '))
#---------------------------------------------------------------------------------------------------------------------#
def incluirTelefone():
    while True:
        print()
        nome = input('Qual contato quer editar? ')
        if nome in lista_contatos.keys():                                   # Função para incluir um telefone em #
            lista_contatos[nome].append(input('Adicionar Telefone: '))      # um contato existente #
            break
        else:
            print('Nome não existente, tente outro')
#---------------------------------------------------------------------------------------------------------------------#
def excluirTelefone():
    while True:
        print()
        nome = input('Qual contato quer editar? ')
        if nome in lista_contatos:                                          # Função para excluir o telefone de #
            for i in range(len(lista_contatos[nome])):                      # um contato existente#
                print(f'{i + 1}: {lista_contatos[nome][i]}')
            delete_tel = int(input('Telefone a ser removido: '))
            del (lista_contatos[nome][delete_tel - 1])
            break
        else:
            print('Nome não existente, tente outro')
#---------------------------------------------------------------------------------------------------------------------#
def excluirNome():
    while True:
        print()
        nome_del = input('Contato a ser excluído: ')                        # Função para excluir o nome um contato #
        if nome_del in lista_contatos.keys():                               # da lista#
            del lista_contatos[nome_del]
            break
        else:
            print('Nome não existente, tente outro')
#---------------------------------------------------------------------------------------------------------------------#
def consultarNome():
    print()
    print('***Lista Completa de Contatos***')
    print()
    for k,v in lista_contatos.items():                                      # Função para listar os contatos existentes#
        print(f'Nome: {k}')
        print('Telefone(s):')
        for i in range (len(v)):
             print(f'{v[i]}')
        print()
#---------------------------------------------------------------------------------------------------------------------#

menuPrincipal()
