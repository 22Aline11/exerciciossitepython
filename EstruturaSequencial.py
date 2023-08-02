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

#