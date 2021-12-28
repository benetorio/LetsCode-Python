tabuada = int(input('Informe um número de 1 a 9: '))

print(f'\tTabuada do número {tabuada}')
for num in range(1,11):
  print(f'{tabuada} * {num}  =  {tabuada * num}')