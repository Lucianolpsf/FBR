# Variaveis e tipos

nome = 'Luciano'
idade = 31
altura = 1.78
trabalhando = True # False
profissao = '' # criando variavel vazia
peso = float() # criando variavel tipificada

# Printando valores

print(nome)
print("Olá, seja bem vindo", nome)
print("Olá, seja bem vindo "+ nome)
print(f'Esta um lindo dia hoje {nome}, não acha?')

# Verificando tipo de uma variavel

print(type(nome))

# Solicitando valores do usuario
nome2 = input("Informe seu nome: ")
print(f'O nome digitado foi {nome2}')

# Algoritimo para soma de dois numeros
numero1 = int(input('Informe o primeiro numero '))
numero2 = int(input('Informe o segundo numero '))
soma = numero1 + numero2
print(f'A soma é: {soma}')

# Caracteres algebricos

'+' # soma
'-' # subtração
'*' # multiplicação
'/' # divisão
'**' # potencia
'//' # divisão inteira

# expressões numericas

resultado = 3*(5*2-1)+2*3-(5+2*6)
print(resultado)
