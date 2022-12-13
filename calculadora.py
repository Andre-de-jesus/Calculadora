import math
import os

vazio = ' '
linha = '-' * 67

while True:
    print(linha)
    print('Calculadora'.center(67))
    print(linha)
    print(vazio)
    print('Digite 1 se você deseja somar')
    print('Digite 2 se você deseja subtrair')
    print('Digite 3 se você deseja multiplicar')
    print('Digite 4 se você deseja dividir')
    print('Digite 5 para calcular juros simples')
    print('Digite 6 para calcular juros compostos')
    print('Digite 7 para calcular porcentagem')
    print('Digite 8 para resolver equação de segundo grau')
    print(vazio)
    print(linha)
    print(vazio)
    escolha = int(input('Digite aqui sua escolha: '))
    os.system('clear') or None
    if escolha == 1:
        soma = []
        valores = int(input('Digite aqui quantos números você deseja somar: '))
        for valor in range (0, valores):
           valores = float(input('Digite aqui o valor {}: '.format(valor + 1)))
           soma.append(valores)
           print(vazio)
           print('O total é {}'.format(sum(soma)))
           print(vazio)
    elif escolha == 2:
        valor1 = float(input('Digite aqui um valor: '))
        valor2 = float(input('Digite aqui outro valor: '))
        print(vazio)
        print('A subtração dos valores é igual a {}'.format(valor1 - valor2))
        print(vazio)
    elif escolha == 3:
        valor1 = float(input('Digite aqui um valor: '))
        valor2 = float(input('Digite outro valor: '))
        print(vazio)
        print('A multiplicação entre {} e {} é {}'.format(valor1, valor2, valor1 * valor2))
        print(vazio)
    elif escolha == 4:
        valor1 = float(input('Digite aqui um valor: '))
        valor2 = float(input('Digite outro valor: '))
        print(vazio)
        print('A divisão entre {} e {} é {}'.format(valor1, valor2, valor1 / valor2))
    elif escolha == 5:
        capital = float(input('Digite aqui o capital inicial: '))
        taxa = float(input('Digite aqui o valor da taxa de juros: '))
        tempo = float(input('Digite aqui o tempo [em meses]: '))
        juros = capital * taxa * tempo
        print(vazio)
        print('O juros do capital {} é igual a {}'.format(capital, juros))
        print(vazio)
    elif escolha == 6:
        valorinicial = float(input('Digite aqui valor inicial: '))
        rentabilidade = float ( input('Rentabilidade mensal: '))
        rentabilidade = rentabilidade / 100
        tempo= int( input('Meses que vai deixar rendendo: '))
        valorfinal = valorinicial * (1+ rentabilidade) ** tempo
        print(vazio)
        print('Valor após {} meses é igual a {}'.format(tempo, valorfinal))
    elif escolha == 7:
        valororiginal = float(input('Digite aqui o valor do produto: '))
        porcentagem = float(input('Digite aqui a porcentagem: '))
        preçofinal = valororiginal * (porcentagem / 100)
        print(vazio)
        print('{} % de {:.2f} R$ é {:.2f} '.format(porcentagem, valororiginal, preçofinal))
    elif escolha == 8:
        a = int(input('Qual o valor de a: '))
        b = int(input('Qual o valor de b: '))
        c = int(input('Qual o valor de c: '))
        delta = b*b - (4*a*c)
        if delta<0:
            print('Delta menor que 0. Raízes imaginárias.')
        if delta==0:
            raiz = -b / (2*a)
            print('Delta=0 , raiz = ',raiz)
        else:
            raiz1 = (-b + math.sqrt(delta) ) / (2*a)
            raiz2 = (-b - math.sqrt(delta) ) / (2*a)
            print('Raizes: ',raiz1,' e ',raiz2)
    print(vazio)
    opção = str(input('Digite [S] se você deseja continuar ou digite [N] se você deseja encerrar o programa: ')).upper()
    os.system('clear') or None
    if opção == 'N':
        break