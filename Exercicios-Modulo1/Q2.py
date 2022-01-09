"""
  Faça um programa que leia a validade das informações:
  a. Idade: entre 0 e 150;
  b. Salário: maior que 0;
  c. Sexo: M, F ou Outro;

  O programa deve imprimir uma mensagem de erro para cada informação inválida.
"""

def teste_idade(idade_informada, min, max):
  if (idade_informada<=min or idade_informada>=max):
    print(f'A idade é invalida. Insira valores entre {min} e {max}.\nPor favor, tente novamente.\n')
  return idade_informada>min and idade_informada<max

def teste_salario(salario_informado, min):
  if (salario_informado<=min):
    print(f'O valor é inválido. Insira valores maiores que {min}.\nPor favor, tente novamente.\n')
  return salario_informado>min

def teste_genero(genero_informado, possibilidades):
  if genero_informado.upper() not in possibilidades:
    print(f'O genero informado não é válido. Insira uma das opções M/F ou Outro.')
    print('tente novamente.')
  return genero_informado.upper() in possibilidades

while(True):
  idade = int(input('Digite a idade:'))
  idade_min, idade_max = 0, 150
  if (teste_idade(idade, idade_min, idade_max)):
    break

while(True):
  salario = float(input('Digite o salario:'))
  salario_min = 0
  if (teste_salario(salario, salario_min)):
    break

while(True):
  generos = ['M', 'F', 'Outro']
  sexo = input(f'Digite o sexo {generos}:\n')
  if (teste_genero(sexo, generos)):
    break

print(f'Sua idade é {idade}')
print(f'Seu salário é {salario}')
print(f'Seu gênero é {sexo}')
