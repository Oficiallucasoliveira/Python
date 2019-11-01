
print(' Exercicio escreva uma expressão para determinar se uma pessoadeve ou nao pagar imposto. considere que pagar imposto pessoas cujo salario e maior que 1200')
salario = 1200
idade = 18
aprovado = True
reprovado = False


meusalario = int(input("Digite seu Salario: "))
minhaidade = int(input("Qual Sua idade: "))


#soma = print(int(meusalario > salario and minhaidade > idade ))


if meusalario > salario and minhaidade > idade:
	print('Aprovado!')
else:
	print('Reprovado!')



