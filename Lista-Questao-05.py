#05 - LISTA DE EXERCÍCIOS

salario001 = int (input('Salário: '))

aumento = int (input('Aumento em porcentagem: '))

salario002 = (aumento / 100 *salario001) + salario001

print('O aumento será de: {:.2f}'.format(aumento /100 * salario001))

print('O novo salário será: {:.2f}'.format(salario002))