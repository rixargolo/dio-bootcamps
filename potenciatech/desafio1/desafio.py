def calc_hamburger(valor_hamburguer, quantidade_hamburguer):
  total_hamburguer = valor_hamburguer * quantidade_hamburguer
  return total_hamburguer
  
def calc_bebida(valor_bebida, quantidade_bebida):
  total_bebida = valor_bebida * quantidade_bebida
  return total_bebida

def total_pedido(total_hamburguer, total_bebida):
    total_pedido = total_hamburguer + total_bebida
    return total_pedido

def calc_troco(total_pedido, valor_pago):
    troco = valor_pago - total_pedido
    return troco
  

def main():
    valorHamburguer = float(10)
    quantidadeHamburguer = int(2)
    valorBebida = float(5)
    quantidadeBebida = int(1)
    valorPago = float(30)
    
    hamburger = calc_hamburger(valor_hamburguer=valorHamburguer, quantidade_hamburguer=quantidadeHamburguer)
    bebida = calc_bebida(valor_bebida=valorBebida, quantidade_bebida=quantidadeBebida)
    total = total_pedido(total_hamburguer=hamburger, total_bebida=bebida)
    troco = calc_troco(total_pedido=total, valor_pago=valorPago)
    
    print(f'O preço final do pedido é R$ {total:.2f}. Seu troco é R$ {troco}.')

main()