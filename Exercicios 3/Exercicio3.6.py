#Exercicio 3.6
print('''Escreva uma expressão que sera ultilizada para decidir se um aluno foi aprovado ou não aprovado.
 Para ser aprovado, todas as medias do aluno devem ser maiores que 7.  Considere que o aluno Cursa apenas
 tres materias e que a nota de cada esta armazenada nas seguintes  
variaveis: materia1, materia2, e materia3

 ''')
materia1 = int(input("Portugues Nota: ")) 
materia2 = int(input("Ingles Nota: ")) 
materia3 = int(input("Matematica Nota: "))


resultado = materia1 + materia2 + materia3

print('Resultado: ', resultado)
if resultado >= 7:
	print('Aluno Aprovado')
else:
	print('Aluno Reprovado!')
