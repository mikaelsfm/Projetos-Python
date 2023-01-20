import random


########################### TABELA DE RESULTADOS ########################################

tabela_completa = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],               #Matriz da classificação zerada,
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],               #marcando as devidas posições
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
for l in range(0,6):
    # Para inserir o nome do piloto #
    tabela_completa[l][0] = input('Nome do piloto: ')
    for c in range(1, 11):
# Número aleatório entre 90 e 120 para definir os tempos das voltas, já deixando com 3 casas decimais #
        tempo = round(((random.random()*30)+90), 3)
        tabela_completa[l][c] = tempo
print ()
print('***Tabela de Resultados***')
# Indo de linha em linha, o print vai mostrando cada um dos tempos de cada piloto #
for l in range (0,6):
    print(f'{tabela_completa[l][0]} - {tabela_completa[l][1]}, {tabela_completa[l][2]}, {tabela_completa[l][3]}, {tabela_completa[l][4]}, {tabela_completa[l][5]}, {tabela_completa[l][6]}, {tabela_completa[l][7]}, {tabela_completa[l][8]}, {tabela_completa[l][9]}, {tabela_completa[l][10]}')
print()


##################### TABELA DE MELHORES VOLTAS ##############################################

tabela_melhor_volta = [[0, 0, 0],
                       [0, 0, 0],
                       [0, 0, 0],
                       [0, 0, 0],
                       [0, 0, 0],
                       [0, 0, 0]]
menor_tempo = 9000 #Variável para depois ser usada na análise da volta mais rápida de cada piloto#
for l in range(0,6):
# Defini a primeira coluna de cada linha usando a anterior, já deixando com o nome dos pilotos #
    tabela_melhor_volta[l][0] = tabela_completa[l][0]
    for c in range(1, 11):
# Condições para analisar qual é o menor tempo de cada piloto
        if tabela_completa[l][c] < menor_tempo:
            menor_tempo = tabela_completa[l][c]
            volta = c
            tabela_melhor_volta[l][2] = menor_tempo
# Inserção da volta que foi mais rápida na matriz de menor volta #
    tabela_melhor_volta[l][1] = volta
# Reset do menor tempo para não haver conflito no loop #
    menor_tempo = 9000

print('***Tabela de Melhores Tempos***')
for l in range(0,6):
    print(f'{tabela_melhor_volta[l][0]} -> volta nº{tabela_melhor_volta[l][1]}, em {tabela_melhor_volta[l][2]}')
print()


########################### TABELA DE CLASSIFICAÇÃO ########################################

# Defini uma nova tabela só para não correr risco de conflito #
tabela_class = tabela_melhor_volta
# Ordenação da coluna 3(menor volta) da menor para a maior, organizando os pilotos baseados na menor volta #
tabela_class.sort(key= lambda aux: aux[2])

print('***Tabela de Classificação***')
for l in range (0,6):
# Print para ordenar os pilotos por suas voltas mais rápidas #
    print(f'{l+1}º Lugar -> {tabela_class[l]}')
print (f'O primeiro do grid de largada foi {tabela_class[0][0]}, tendo o tempo de {tabela_class[0][2]} segundos na {tabela_class[0][1]}ª volta')
print()


######################### TABELA DAS MÉDIAS ##########################################

# 0 só para definir algo à variável #
soma = 0
# Tabela para as médias, com 10 linhas e 1 coluna #
tabela_medias = [[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]]
#Loop para fazer a soma de cada tempo por volta #
for c in range(1,11):
    for l in range (0,6):
        soma = soma + tabela_completa[l][c]
    media = soma/6          # média de cada volta
    media = round(media,3)  # definição de 3 casas decimais
    tabela_medias[c-1][0] = media
# Reset da soma para não haver conflito no loop #
    soma = 0

print('***Tabela das médias de tempo em cada volta***')
# Print das médias de cada volta #
for l in range(0,10):
    print (f'Média da {l+1}ª volta: {tabela_medias[l][0]} segundos')


