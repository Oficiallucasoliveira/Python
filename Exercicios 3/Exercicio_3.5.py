#Exercicio 3.5
print('Calcule o resultado da expressao A > b and C or D, Ultilizando os valores da tabela a seguir \n')


#tabela
print("""A  | B  | C    | D     | Resultado|\n
1  | 2  | True | False | False    |\n
10 | 3  | False| False | False    |\n
5  | 1  | True | True  | True     |\n
""")
#listas 
a = 1
b = 2
c = True
d = False

primeirasoma = a > b and c or d
print('Primeira soma resposta: ', primeirasoma)
#lista2 
a = 10
b = 3
c = False
d = False
segundasoma = a > b and c or d
print('Segunda soma resposta: ', segundasoma)

#lista2 
a = 5
b = 1
c = True
d = True
terceirasoma = a > b and c or d
print('Terceira soma resposta: ', terceirasoma)
