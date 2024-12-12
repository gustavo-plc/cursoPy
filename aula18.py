from aula16 import pessoa

teste = list() #criação da lista
teste.append('Gustavo') #inserção do 1º elemento
teste.append(40) #inserção do 2º elemento

print(teste)

galera = list() #criação de uma segunda lista

galera.append(teste) # inserção da lista teste como 1º elemento da lista galera
#NO APPEND É FEITA UMA LIGAÇÃO ENTRE AS DUAS ESTRUTURAS

#INSERINDO COMO CÓPIA
galera.append(teste[:]) #inserção de um segundo elemento na lista galera, COMO CÓPIA, ou seja, não é feito um link

print(galera)
#alteração de dados da lista teste, que está dentro da lista galera
#quando altero a lista raiz, as outras que a contém também são alteradas, caso inseridas como link
teste[0] = 'Maria'
teste[1] = 22

print(teste) #printa a alteração já feita, ou seja, printa maria
print(galera) #como o append foi feito como link e depois como cópia, a alteração da lista teste só se refletirá no dado da lista galera inserido como link, ou seja, no primeiro.
#então o primeiro elemento vira maria, e o segundo permanece Gustavo, porque foi inserido como cópia.
print('\n')

#outra forma de declarar
pessoas = [['João', 19],['Ana', 33],['Joaquim', 13],['Maria', 45]]
print(pessoas)
print(pessoas[0])
print(pessoas[0][0])
print(pessoas[0][1])
print(pessoas[2][0])

for p in pessoas: #printa cada elemento da lista
    print(p)

for p in pessoas: #printa somente o nome das pessoas, pq estão na posição 0 da lista
    print(p[0])

for p in pessoas: #printa somente a idade das pessoas, que estão na posição 1
    print(p[1])

for p in pessoas:
    print(f'{p[0]} tem {p[1]} anos')

    #exemplo de leitura de dados

people = list()
pearson = list() #lista secundária, para armazenamento temporário
totmaior = totmenor = 0
for i in range(0, 3):
    pearson.append(str(input('Nome: ')))
    pearson.append(int(input('Idade: ')))
    people.append(pearson[:]) #mandando os dados como cópia, pq serão apagados em seguida
    pearson.clear()

for p in people:
    if p[1] <= 21:
        print(f'{p[0]} é menor de idade')
        totmenor += 1
    else:
        print(f'{p[0]} é maior de idade')
        totmaior += 1

print(f'Temos {totmaior} maiores de idade e {totmenor} menores de idade')