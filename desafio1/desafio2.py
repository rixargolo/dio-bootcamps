import textwrap
import os

def menu():
  menu = """\n
  =============== MENU ===============
  [d]\tDepositar
  [s]\tSavar
  [x]\tExtrato
  [nc]\tNova conta
  [lc]\tListar contas
  [nu]\tNovo usuário
  [q]\tSair
  ==> """
  return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
  os.system('cls')
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
  return saldo 

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
  os.system('cls')
  excedeu_saldo = valor > saldo
  excedeu_limite = valor > limite
  excedeu_saques = numero_saques >= limite_saques
  
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
      
  return saldo, extrato      
    
def exibir_extrato(saldo, /, *, extrato):
  os.system('cls')
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

def criar_usuario(usuarios):
  os.system('cls')
  cpf = input('Informe o CPF (somente números): ')
  usuario = filtrar_usuario(cpf, usuarios)
  
  if usuario:
    print('!! Falha na operação !!\n Este CPF já está cadastrado!')
    input('Pressione ENTER para retornar ao menu...')
    os.system('cls')
    return

def filtrar_usuario(cpf, usuarios):
  return

def criar_conta(agencia, numero_conta, usuarios):
  return

def listar_contas():
  return


def main():
  LIMITE_SQUES = 3
  AGENCIA = '0001'
  
  saldo = 0
  limite = 500
  extrato = []
  numero_saques = 0
  usuarios = []
  contas = []
  
  while True:
    opcao = menu()
    
    if opcao == 'd':
      valor = float(input('Informe o valor para depósito: '))
      
      saldo, extrato = depositar(saldo, valor, extrato)      
    
    elif opcao == 's':
      valor = float(input('Informe o valor do saque: '))
      
      saldo, extrato = sacar(
        saldo=saldo,
        valor=valor,
        extrato=extrato,
        limite=limite,
        numero_saques=numero_saques,
        limite_saques=LIMITE_SQUES,
      )

    elif opcao == 'x':
      exibir_extrato(saldo, extrato=extrato)

    elif opcao == 'nc':
      numero_conta = len(contas) + 1
      conta = criar_conta(AGENCIA, numero_conta, usuarios)
      
      if conta:
        contas.append(conta)
    
    elif opcao == 'lc':
      listar_contas(contas)    

    elif opcao == 'nu':
      criar_usuario(usuarios)
    
    elif opcao == 'q':
      os.system('cls')
      print('\n\nObrigado por utilizar nosso Banco :)\n\n')
      break

main()