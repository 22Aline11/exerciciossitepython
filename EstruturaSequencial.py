# 1. Faça um Programa que mostre a mensagem "Alo mundo" na tela. 
print("Alo mundo!")

#2. Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número]. 
numero = int(input("Escreva um número: "))
print("O número digitado foi ", numero)

#3. Faça um Programa que peça dois números e imprima a soma. 
num_1 = int(input("Coloque o primeiro número: "))
num_2 = int(input("Coloque o segundo número: "))
soma = num_1 + num_2
print("O valor total é: ", soma)

#4. Faça um Programa que peça as 4 notas bimestrais e mostre a média. 
nota_1 = int(input("Primeira nota: "))
nota_2 = int(input("Segunda nota: "))
nota_3 = int(input("Terceira nota: "))
nota_4 = int(input("Quarta nota: "))
media = int((nota_1 + nota_2 + nota_3 + nota_4) / 4)

print(media)

#5. Faça um Programa que converta metros para centímetros. 
metro = int(input("Coloque o número de metros: "))
centimetros = 100
conversao = metro * centimetros
print( metro, "metros são", conversao, "centimetros.")

#6. Faça um Programa que peça o raio de um círculo, calcule e mostre sua área. 
raio = int(input("Coloque o raio do circulo: "))
area = (raio * raio) * 3.14
print(area)

#7. Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário. 
lado = int(input("Coloque o valor de um lado do quadrado: "))
area = lado * lado
dobro_area= area * 2 
print("A área do quadrado é:", area, ". O dobro da área é: ", dobro_area)

#8. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês. 
sal_hora = float(input("Qual valor você por hora? "))
horas_mes = float(input("Qual total de horas trabalhadas no mês? "))
salario = float(sal_hora * horas_mes)
print("Seu salário é de R$ {:.2f}".format(salario))

#9. Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.

temp_f = float(input("Coloque a temperatura em Fahreheint: "))
temp_c = 5 * ((temp_f-32) / 9)

print (" A temperatura em Celsius é: {:.1f}".format(temp_c))

# 10.Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit. 
temp_c = float(input("Coloque a temperatura em Celsius: "))
temp_f = (temp_c * 9 / 5) + 32

print(" A temperatura em Fahrenheit é: {:.1f}".format(temp_f))

#11. Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
    #a. o produto do dobro do primeiro com metade do segundo.
    #b. a soma do triplo do primeiro com o terceiro.
    #c. o terceiro elevado ao cubo. 
int_1 = int(input("Adicione o primeiro número inteiro: "))
int_2 = int(input("Adicione o segundo número inteiro: "))
float_1 = float(input("Adicione um número real: "))

a = (int_1 *2) * (int_2 / 2 )
print(a)

b = (int_1 * 3) + float_1
print(b)

c = float_1 ** 3
print(c)

# 12. Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58 
altura = float(input("Coloque a sua altura: "))
peso_ideal = (72.7 * altura) - 58 
print("{:.1f}".format(peso_ideal))

# 13. Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:

    #Para homens: (72.7*h) - 58
    #Para mulheres: (62.1*h) - 44.7 

sexo = input("Qual o seu sexo? ").lower()
altura = float(input("Coloque a sua altura: "))

if sexo == "feminino":
    peso_fem = (62.1 * altura) - 44.7 
    print("De acordo com o gênero feminino o seu peso ideial é: {:.1f}".format(peso_fem))
else:
    peso_masc = (72.7 * altura) - 58
    print("De acordo com o gênero masculino o seu peso ideial é: {:.1f}".format(peso_masc))


# 14. João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. 
# Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente.
#  João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. 
# Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. 
# Imprima os dados do programa com as mensagens adequadas. 

peso_pescado = float(input("Coloque os quilos de peixe pescados hoje: "))
peso_limite = 50
excedente = peso_pescado - peso_limite
taxa_multa = 4

if peso_pescado > peso_limite:
    multa_pagar = abs(excedente) * taxa_multa
    print("Os quilos de pesca excedidos são: {:.1f}".format(abs(excedente))) #abs força a aparecer positivo mesmo que seja negativo
    print("Multa a pagar R$ {:.2f}".format(multa_pagar))
else:
    print("Pesca dentro do limite permitido.")

# 15. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, 
# sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:

    #salário bruto.
    #quanto pagou ao INSS.
    #quanto pagou ao sindicato.
    #o salário líquido.
    #calcule os descontos e o salário líquido, conforme a tabela abaixo:

    #+ Salário Bruto : R$
    #- IR (11%) : R$
    #- INSS (8%) : R$
    #- Sindicato ( 5%) : R$
    #= Salário Liquido : R$

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

#16. Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. 
# Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total. 
import math

area = float(input("Coloque a área a ser pintada em metros quadrados: "))
litros = area / 3
lata_tinta = math.ceil(litros / 18)
unidade = 80

if litros <= 18:
    print("Compre 1 galão de tinta")
    print("Preço total: R$ {:.2f}".format(unidade))
else:
    latas_adicionais = lata_tinta - 1 if litros % 18 == 0 else lata_tinta
    preco_total = latas_adicionais * unidade
    print("Compre {} galões de tinta".format(latas_adicionais))
    print("Preço total: R$ {:.2f}".format(preco_total))