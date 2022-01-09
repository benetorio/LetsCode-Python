"""
  Vamos fazer um programa para verificar quem é o assassino de um crime.
  Para descobrir o assassino, a polícia faz um pequeno questionário com 5 perguntas onde a resposta só pode ser sim ou não:
  a. Mora perto da vítima?
  b. Já trabalhou com a vítima?
  c. Telefonou para a vítima?
  d. Esteve no local do crime?
  e. Devia para a vítima?
  Cada resposta sim dá um ponto para o suspeito. A polícia considera que os suspeitos com 5 pontos são os assassinos, com 4 a 3 pontos são cúmplices e
  2 pontos são apenas suspeitos, necessitando outras investigações. Valores iguais ou abaixo de 1 são liberados.
"""

perguntas = ['Mora perto da vítima? ', 
             'Já trabalhou com a vítima? ', 
             'Telefonou para a vítima? ', 
             'Esteve no local do crime? ', 
             'Devia para a vítima? ']

pontos = 0 

def suspeito(pontos):
  if pontos <= 1:
    return 'Liberado.'
  elif pontos == 2:
    return 'Suspeito.'
  elif pontos <= 4:
    return 'Cúmplice.'
  elif pontos == 5:
    return 'Assassino.'

print("Responda todas as perguntas a seguir com S para Sim ou N para Não.\n")
for pergunta in perguntas: 
  if input(pergunta).upper() == 'S':
  pontos +=1

print(f'Você está sendo considerado como', suspeito(pontos))