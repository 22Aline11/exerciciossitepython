sal_hora = float(input("Qual valor você por hora? "))
horas_mes = float(input("Qual total de horas trabalhadas no mês? "))
salario_bruto = float(sal_hora * horas_mes)
inss = ((11 * salario_bruto) / 100)
ir = ((8 * salario_bruto) / 100)
sindicato = ((5 * salario_bruto) / 100)
salario_liq = salario_bruto - inss - sindicato
print("Salário Bruto : R$ {:.2f}".format(salario_bruto))
print("IR (11%) : R$  {:.2f}".format(ir))
print("INSS (8%) : R$  {:.2f}".format(inss))
print("Sindicato ( 5%) : R$ {:.2f}".format(sindicato))
print("Salário Liquido : R$  {:.2f}".format(salario_liq))