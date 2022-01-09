"""
  Faça um programa que imprima a tabuada do 9 (de 9*1 a 9*10) usando loops.
"""

tabuada = int(input('Informe um número de 1 a 9: '))

print(f'\tTabuada do número {tabuada}')
for num in range(1,11):
  print(f'{tabuada} * {num}  =  {tabuada * num}')