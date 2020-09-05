lista_1 = [6,8,10,13,16,18,26, 30, 29, 31]
lista_2 = [6,8,10,13,16,18,26, 30, 29, 31]
listas_de_pedido = [lista_1, lista_2]

def criar_pedido(pedidos: []):
    lista_de_pedido_final = []
    for pedido in pedidos:
        for prato in pedido:
            lista_de_pedido_final = \
                verificar_se_numero_de_pedido_ja_existe_na_lista_de_pedidos(
                    prato,
                    lista_de_pedido_final
                )
    return lista_de_pedido_final



def verificar_se_numero_de_pedido_ja_existe_na_lista_de_pedidos(
        numero_do_pedido: int,
        lista_de_pedido_final: [],
):
    if lista_de_pedido_final:
        for pedido in lista_de_pedido_final:
            if numero_do_pedido == pedido['prato']:
                pedido['quantidade'] = pedido['quantidade'] + 1
            else:
                lista_de_pedido_final.append({'prato': numero_do_pedido, 'quantidade': 1})
    else:
        lista_de_pedido_final.append({'prato': numero_do_pedido, 'quantidade': 1})
    return lista_de_pedido_final


print(len(criar_pedido(listas_de_pedido)))