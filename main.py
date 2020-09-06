from pedido import criar_pedido, quantidade_de_pratos, gerar_pedido

quantidade_de_pedidos = input('Insira a quantidade de pedidos:')
listas_de_pedido = []
for i in range(int(quantidade_de_pedidos)):
    pedido_iput = input('Insira o número do pedido separado por vírgula:')
    listas_de_pedido.append(pedido_iput.split(','))
    print(listas_de_pedido)


pedidos = criar_pedido(listas_de_pedido)
print("quantidade:", quantidade_de_pratos(pedidos))
gerar_pedido(pedidos)