#Questão 17

espaco = int(input())
tempo = int(input())

vm = espaco/tempo
print("A velocidade média é:",vm)

#Questão 18

idade = int(input())

idadedias = idade * 365

print("A idade informada, em dias é",idadedias)

#Questão 19

dia = 24
diasegundos = 24 * 3600

print("A quantidade de segundos em um dia é:",diasegundos)

#Questão 20

peso = int(input())
altura = int(input())

imc = peso/altura
print("O imc é:",imc)

#Questão 21

difnum1 = int(input())
difnum2 = int(input())

diferençatotal = difnum1 - difnum2
print("A diferença entre dois numeros são:"<diferençatotal)

#Questão 22

divint1 = int(input())
divint2 = int(input())

divinteira = divint1/divint2
print("O resultado da divisao inteira é:",int(divinteira))

#Questão 23 

numero = int(input())
valorabsoluto = abs(numero)
print("O valor absoluto do numero informado é:",valorabsoluto)

#Questão 24

kmh = int(input())
ms = kmh * 0.277778

print("m/s são",ms)

#Questão 25

a = float(input('Entre com o valor de a: '))
b = float(input('Entre com o valor de b: '))
c = float(input('Entre com o valor de c: '))

delta = (b ** 2) - 4 * a * c

print("\n**************************\n")

x1 = (-b + delta ** (1 / 2)) / (2 * a)
x2 = (-b - delta ** (1 / 2)) / (2 * a)

print("o x1 é",x1)
print("o x2 é",x2)

#Questão 26

prod1 = float(input())
prod2 = float(input())
prod3 = float(input())

compra = prod1+prod2+prod3
print("A compra total deu:",compra)

#Questão 27

def converter_dias_para_semanas_e_dias(dias):
    semanas = dias // 7
    dias_restantes = dias % 7
    return semanas, dias_restantes

dias_input = int(input("Digite o número de dias: "))
semanas, dias_restantes = converter_dias_para_semanas_e_dias(dias_input)

print(f"{dias_input} dias = {semanas} semanas e {dias_restantes} dias")

#Questão 28

valor = float(input())

if(valor > 100.0):
    descprog = valor - (valor * 0.10)
else:
    descprog = valor - (valor * 0.5)

print("O desconto progressivo é:",descprog)

#Questão 29

numlim1 = int(input())
numlim2 = int(input())

divcasalim = numlim1/numlim2
print(f'O resultado é{divcasalim:.3}')