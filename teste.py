# 10.Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit. 
temp_c = float(input("Coloque a temperatura em Celsius: "))
temp_f = (temp_c * 9 / 5) + 32

print(" A temperatura em Fahrenheit é: {:.1f}".format(temp_f))