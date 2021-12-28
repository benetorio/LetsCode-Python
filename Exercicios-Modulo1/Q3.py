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