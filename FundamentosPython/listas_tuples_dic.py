# # Lista =  Vários itens mutáveis, dá pra usar append (ex.: preços, inflação, etc.).
# # Tuplas = Um ou vários itens imutáveis, não da pra usar append (ex.: meses, dias da semana, etc).
# # Dicionários = Armazenas um item relacionado à um chave (ex.: usuários, endereços, produtos, configurações, etc.)


# # LISTA

# tarefas = []

# tarefas.append('Ler livro')
# tarefas.append('Estudar SQL')
# tarefas.append('Estudar Python')

# # print(tarefas)
# # print(tarefas[0])
# # print(tarefas[1])
# # print(tarefas[2])

# # Aqui ele vai contador em número a quantidade de tarefas, e não quais são elas.
# # for tarefa in range (3):
# #    print(f'Tarefa: {tarefas}')

# print('Minhas tarefas de hoje: ')
# for tarefa in tarefas:
#     print(f'Tarefa: {tarefa}')

# print('------------------------------------------')

# # TUPLA

# meses = ('Janeiro', 'Fevereiro', 'Março')
# print(meses)

# print('------------------------------------------')

# # DICIONÁRIO
# # usuario = {
# #     'nome': 'Miguel',
# #     'idade': '18',
# #     'departamento': 'TI'
# # }

# # print(usuario['nome'])
# # print(usuario['departamento'])
# # print(usuario['idade'])

# # usuario['idade'] = 35 # Alterar
# # print(usuario['idade'])
# # usuario['cidade'] = 'Toledo'
# # print(usuario['cidade'])

# print('------------------------------------------')


# # Cadastro de Aluno na Faculdade
aluno = {
    'nome': str(input('Digite seu nome completo: ')),
    'idade': int(input('Digite sua idade: ')),
    'curso': str(input('Digite seu curso: '))
}

professores = []

professores.append('William')
professores.append('Rosângela')
professores.append('Wesley')

for professor in professores:
    print(f'Professor(a): {professor}')

if aluno['idade'] < 18:
    print('Você ainda é menor de idade, não completou o ensino médio. Volte para a escola!')
else:
    print('Bem-vindo à faculdade!')