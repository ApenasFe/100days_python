import time
import os
clear = lambda: os.system('cls') #on Windows System
os.system('clear') #on Linux System
clear()

#Printar uma introdução
print("Bem-vindo(a) à calculadora de gorjeta!")

#Pedir o valor total da conta
Conta = input("Qual o valor total da conta?\n")
Conta = float(Conta)
#print(Conta)
clear()

#Perguntar porcentagem da gorjeta
GorjetaPorcentagem = input("Qual a porcentagem de gorjeta? 10, 12 ou 15%\n")
GorjetaPorcentagem = int(GorjetaPorcentagem)
GorjetaResultado = GorjetaPorcentagem * Conta / 100
GorjetaAcrescentada = Conta + GorjetaResultado
#print(GorjetaAcrescentada)
clear()

#Perguntar em quantas pessoas será dividida
TotalPessoas = input("A conta será dividida em quantas pessoas?\n")
TotalPessoas = float(TotalPessoas)
Divisao = GorjetaAcrescentada / TotalPessoas
#print(Divisao)
clear()

#Mostrar o resultado do calculo de quanto cada pessoa deve pagar
ContaTotal = round(Divisao, 2)
print(f"Cada pessoa deve pagar R${ContaTotal}")
time.sleep(300)