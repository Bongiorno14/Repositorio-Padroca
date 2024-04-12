# importando a biblioteca logging para poder usá-la
import logging

# configurando para que minha biblioteca logging
# toda vez que for chamada imprima no terminal
logging.basicConfig(level=logging.INFO)

# Adicionei o tipo de dado esperado em cada argumento
# da sua função, é uma ótima prática para evitar
# seu código quebrar por esse erro
def calcular_pedido(
    valorHamburguer: float,
    quantidadeHamburguer: int,
    valorBebida: float,
    quantidadeBebida: int,
    valorPago: float,
):
    """__Sumary__Escrever de forma resumida o que sua função faz

    Args: Aqui vc descreve as entradas da função e o tipo de dado esperado
        valorHamburguer (float): _description_
        quantidadeHamburguer (int): _description_
        valorBebida (float): _description_
        quantidadeBebida (int): _description_
        valorPago (float): _description_

    Returns: Aqui vc explica o tipo do retorno e dá detalhe sobre ele
        _type_: _description_
    """

    total_hamburgueres = valorHamburguer * quantidadeHamburguer
    total_bebidas = valorBebida * quantidadeBebida
    preco_total_pedido = total_hamburgueres + total_bebidas
    troco = valorPago - preco_total_pedido
    
    # Quebrei a string do retorno da função para cada linha ter
    # Menos do q 88 caracteres (padrão Pep8 (padrão mundial))
    return (
        f"O preço final do pedido é R$ {preco_total_pedido:.2f}."
        f" Seu troco é R$ {troco:.2f}."
    )

# Abaixo uma outra forma e fazer mais do dia a dia
def calcular_pedido2(
    valorHamburguer: float,
    quantidadeHamburguer: int,
    valorBebida: float,
    quantidadeBebida: int,
    valorPago: float,
):
    """__Sumary__Escrever de forma resumida o que sua função faz

    Args: Aqui vc descreve as entradas da função e o tipo de dado esperado
        valorHamburguer (float): _description_
        quantidadeHamburguer (int): _description_
        valorBebida (float): _description_
        quantidadeBebida (int): _description_
        valorPago (float): _description_

    Returns: Aqui vc explica o tipo do retorno e dá detalhe sobre ele
        _type_: _description_
    """

    total_hamburgueres = valorHamburguer * quantidadeHamburguer
    total_bebidas = valorBebida * quantidadeBebida
    preco_total_pedido = total_hamburgueres + total_bebidas
    troco = valorPago - preco_total_pedido
    
    # Quebrei a string do retorno da função para cada linha ter
    # Menos do q 88 caracteres (padrão Pep8 (padrão mundial))
    # Utilizar a biblioteca logging é mais indicado quando
    # Se deseja imprimir algo na tela ao invés do return
    # Possui mto mais compatibilidade com infinitas ferramentas
    logging.info(f"final do pedido é R$ {preco_total_pedido:.2f}."
        f" Seu troco é R$ {troco:.2f}."
    )
