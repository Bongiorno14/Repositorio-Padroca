# Na linha abaixo trazemos de dentro do arquivo_de_backend
# apenas a função que deseja usar
# dessa forma separamos o que é backend da execução do script
from arquivo_de_backend import calcular_pedido, calcular_pedido2

# Deixarei comentado as linhas abaixo apenas para mostrar que
# no dia a dia não é necessário deixar essas variéveis criadas
# com o valor que vc deseja usar, quando vc criou sua função
# o nome de cada argumento e sua descrição já diz para o usuário
# o que cada valor significa

# valorHamburguer1 = 8.00
# quantidadeHamburguer1 = 1
# valorBebida1 = 4.00
# quantidadeBebida1 = 4
# valorPago1 = 50.00

resultado1 = calcular_pedido(
    8.00, 1, 4.00, 4, 50.00
)
print(resultado1)

valorHamburguer2 = 15.00
quantidadeHamburguer2 = 3
valorBebida2 = 6.00
quantidadeBebida2 = 2
valorPago2 = 60.00

resultado2 = calcular_pedido(
    valorHamburguer2, quantidadeHamburguer2, valorBebida2, quantidadeBebida2, valorPago2
)
print(resultado2)

# Uma outra forma de fazer o que vc está fazendo
# sem precisar salvar o retorno da função em uma variável
print(calcular_pedido(
    8.00, 1, 4.00, 4, 50.00
))

# Observe que aqui não precisamos do print para ter
# A msg impressa no terminal pq essa função foi escrita
# com a biblioteca logging
calcular_pedido2(
    8.00, 1, 4.00, 4, 50.00
)
