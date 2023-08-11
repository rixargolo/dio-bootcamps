import textwrap
import os
#Este código vai funcionar 100% apenas no Windows

def menu():
  os.system('cls')
  menu = """\n
  =============== MENU ===============
  [d]\tDepositar
  [s]\tSacar
  [x]\tExtrato
  [nc]\tNova conta
  [lc]\tListar contas
  [nu]\tNovo usuário
  [q]\tSair
  ==> """
  return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
  if valor > 0:
    saldo += valor
    extrato.append(f'Depósito: R$ {valor:.2f}')
    print(f'O valor de R$ {valor:.2f} foi depositado em sua conta.\n')
    input('Pressione ENTER para retornar ao menu...')
    os.system('cls')
  else:
    print('!! Falha na operação !! Valor informado não é válido :(\n')
    input('Pressione ENTER para retornar ao menu...')
    os.system('cls')
  return saldo, extrato 

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
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
  
  nome = input('Informe seu nome completo: ')
  data_nascimento = input('Informe sua data de nascimento (dd/mm/aaa): ')
  email = input('Informe seu email: ')

  usuarios.append({'nome': nome, 'data_nascimento': data_nascimento, 'cpf': cpf, 'email': email})

  print(':: Usuário criado com sucesso! ::\n')
    
def filtrar_usuario(cpf, usuarios):
  usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
  return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
  cpf = input('Informe o CPF do usuário: ')
  usuario = filtrar_usuario(cpf, usuarios)
  
  if usuario:
    print('\n:: Conta criada com sucesso! ::')
    return {'agencia': agencia, 'numero_conta': numero_conta, 'usuario': usuario}

print('\n!! Falha na operação !!\n Usuário não encontrado - A conta não foi criada')

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
      os.system('cls')
      valor = float(input('Informe o valor para depósito: '))
      
      saldo, extrato = depositar(saldo, valor, extrato)      
    
    elif opcao == 's':
      os.system('cls')
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
    
    else:
      print('A letra informada não é válida')
      input('Pressione ENTER para retornar ao menu...')
      os.system('cls')      

main()