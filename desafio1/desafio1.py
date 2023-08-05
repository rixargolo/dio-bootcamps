import os

LIMITE_SAQUES = 3

saldo = 0
limite_valor_saque = 500
numero_saques = 0

extrato = []

menu =  '''
    BEM-VINDO AO MENU DO BANCO
    
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [x] Sair    
    
    Escolha uma opção: '''
     
while True:
    
    opcao = input(menu)
    
    if opcao == 'd':
        valor = float(input('Informe o valor do depósito: '))
        
        if valor > 0:
            saldo += valor
            extrato.append(f'Depósito: R$ {valor:.2f}')
            print(f'O valor de R$ {valor:.2f} foi depositado em sua conta.')
            input('Pressione ENTER para retornar ao menu...')
            os.system('cls')
        
        else:
            print('!! Falha na operação !! Valor informado não é válido :(')
            input('Pressione ENTER para retornar ao menu...')
            os.system('cls')
    
    elif opcao == 's':
        valor = float(input('Informe o valor do saque: '))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite_valor_saque
        excedeu_saques = numero_saques >= LIMITE_SAQUES
        
        if excedeu_saldo:
            print('!! Falha na operação !!\n Você não tem saldo suficiente!')
            input('Pressione ENTER para retornar ao menu...')
            os.system('cls')
            
        elif excedeu_limite:
            print('!! Falha na operação !!\n O valor do saldo excede o limite disponível!')
            input('Pressione ENTER para retornar ao menu...')
            os.system('cls')
        
        elif excedeu_saques:
            print('!! Falha na operação !!\n Você não tem mais saques disponíveis hoje!')
            input('Pressione ENTER para retornar ao menu...')
            os.system('cls')
        
        elif valor > 0:
            saldo -= valor
            extrato.append(f'Saque: R$ {valor:.2f}')
            numero_saques += 1
            print(f'O valor de R$ {valor:.2f} foi sacado de sua conta.\n Seu novo saldo é R$ {saldo:.2f}\n\n')
            input('Pressione ENTER para retornar ao menu...')
            os.system('cls')
        
        else:
            print('!! Falha na operação !!\n Valor informado não é válido :(')
            input('Pressione ENTER para retornar ao menu...')
            os.system('cls')
    
    elif opcao == 'e':
        print('\n=================== EXTRATO ===================')
        if extrato == []:
            print('Nenhuma transação encontrada')
        else:
            for item in extrato:
                print(item)
            print(f'\nSaldo atual: R$ {saldo:.2f} ')
        print('\n===============================================')
        input('Pressione ENTER para retornar ao menu...')
        os.system('cls')
    
    if opcao == 'x':
        print('\n\nObrigado por utilizar nosso Banco :)\n\n')
        break