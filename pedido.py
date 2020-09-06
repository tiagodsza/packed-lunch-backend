lista_1 = [6,6,10,13,16,18,26, 30, 29, 31]
lista_2 = [6,6,10,13,16,18,33, 30, 29, 31]
listas_de_pedido = [lista_1, lista_2]

def criar_pedido(pedidos: []):
    lista_de_pedido_final = []
    for pedido in pedidos:
        for prato in pedido:
            if lista_de_pedido_final:
                exists = False
                for prato_lista in lista_de_pedido_final:
                    if prato == prato_lista['prato']:
                        prato_lista['quantidade'] += 1
                        exists = True
                if not exists:
                    lista_de_pedido_final.append({'prato': prato, 'quantidade': 1})
            else:
                lista_de_pedido_final.append({'prato':prato, 'quantidade':1})
    return lista_de_pedido_final

def quantidade_de_pratos(lista_de_pedidos_final: []):
    quantidade = 0
    if lista_de_pedidos_final:
        for pedido in lista_de_pedidos_final:
            quantidade += pedido['quantidade']
    return quantidade

def gerar_pedido(lista_de_pedidos_fnal: []):
    for pedido in lista_de_pedidos_fnal:
        print(f'{pedido["prato"]} { "(" + str(pedido["quantidade"]) + ")" if pedido["quantidade"] > 1 else ""}' )

pedidos = criar_pedido(listas_de_pedido)
print("quantidade:", quantidade_de_pratos(pedidos))
gerar_pedido(pedidos)
