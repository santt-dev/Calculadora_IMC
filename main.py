#criar uma calculadora de IMC
 
def calcular_imc():
    nome = input('Qual seu nome:\n')
    peso = float(input("Qual seu peso?:\n"))
    altura = float(input("Qual sua altura: \n"))
    imc = peso / (altura ** 2 )
    print(f'Olá {nome}, seu IMC é {imc:.2f}')

calcular_imc()