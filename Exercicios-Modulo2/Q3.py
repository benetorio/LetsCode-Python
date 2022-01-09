"""
    Criar uma função que recebe duas listas e 
    retorna a soma item a item dessas listas.
    Exemplo: Se a função receber as listas [1,4,3] e [3,5,1], 
    então a função deve retornar [1+3, 4+5, 3+1] = [4, 9, 4].
"""
lista_1=[1,4,3]
lista_2=[3,5,1]
soma_listas=[]

print('Lista 1 = ', lista_1)
print('Lista 2 = ', lista_2)

if len(lista_1) == len(lista_2):
  for num in range(len(lista_1)):
    soma_listas.append(lista_1[num]+lista_2[num])
  print('A soma das listas ', soma_listas)
else:
  print("Listas de tamanho diferentes.")