Questao 1
Desafio
Você está criando um aplicativo de entrega de comida e precisa calcular o preço final do pedido do usuário. O usuário escolheu alguns itens do cardápio e é preciso calcular o preço total do pedido.

Entrada:
A entrada deve receber os valores abaixo:

valorHamburguer: o valor unitário de um hambúrguer.
quantidadeHamburguer: a quantidade de hambúrgueres que o usuário deseja.
valorBebida: o valor unitário de uma bebida.
quantidadeBebida: a quantidade de bebidas que o usuário deseja.
valorPago: o valor pago pelo usuário.
Saída:
A saída deve retornar um texto informando o valor total do pedido e a quantidade de troco que será necessário. Por exemplo, se tivermos os seguintes valores de entrada:

valorHamburguer = 10.00;
quantidadeHamburguer = 2;
valorBebida = 5.00;
quantidadeBebida = 1;
valorPago = 30.00;
De acordo com esses valores de entrada, o cálculo do preço final do pedido ficaria assim:

Valor total dos hambúrgueres: 10.00 * 2 = 20.00
Valor total da bebida: 5.00 * 1 = 5.00
Preço total do pedido: 20.00 + 5.00 = 25.00
Troco necessário: 30.00 - 25.00 = 5.00
Como o usuário pagou R$ 30.00 e o preço total do pedido ficou em R$ 25.00, o troco necessário é de R$ 5.00. Portanto, a saída esperada para esse exemplo seria:

O preço final do pedido é R$ 25.00. Seu troco é R$ 5.00.

Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

Entrada	Saída
10.00 2 5.00 1 30.00	O preço final do pedido é R$ 25.00. Seu troco é R$ 5.00.
15.00 3 6.00 2 60.00 O preço final do pedido é R$ 57.00. Seu troco é R$ 3.00.
8.00 1 4.00 4 50.00 O preço final do pedido é R$ 24.00. Seu troco é R$ 30.00.

Esse é o code que eu fiz...

def calcular_pedido(valorHamburguer, quantidadeHamburguer, valorBebida, quantidadeBebida, valorPago):
    total_hamburgueres = valorHamburguer * quantidadeHamburguer
    total_bebidas = valorBebida * quantidadeBebida
    preco_total_pedido = total_hamburgueres + total_bebidas
    troco = valorPago - preco_total_pedido
    
    return f"O preço final do pedido é R$ {preco_total_pedido:.2f}. Seu troco é R$ {troco:.2f}."

# Exemplo de uso da função
valorHamburguer1 = 8.00
quantidadeHamburguer1 = 1
valorBebida1 = 4.00
quantidadeBebida1 = 4
valorPago1 = 50.00

resultado1 = calcular_pedido(valorHamburguer1, quantidadeHamburguer1, valorBebida1, quantidadeBebida1, valorPago1)
print(resultado1)

valorHamburguer2 = 15.00
quantidadeHamburguer2 = 3
valorBebida2 = 6.00
quantidadeBebida2 = 2
valorPago2 = 60.00

resultado2 = calcular_pedido(valorHamburguer2, quantidadeHamburguer2, valorBebida2, quantidadeBebida2, valorPago2)
print(resultado2)


Desafio 2

Desafio
Faça um programa que calcule e imprima o salário a ser transferido para um funcionário.

Para realizar o calculo receba o valor bruto do salário e o adicional dos benefícios.
O salário a ser transferido é calculado da seguinte maneira: 

(valor bruto do salário - percentual de imposto mediante ao salário) + adicional dos benefícios

Para calcular o percentual de imposto segue as aliquotas:

    De R$ 0.00 a R$ 1100.00 = 5.00%
    De R$ 1100.01 a R$ 2500.00 = 10.00%
    Maior que R$ 2500.00 = 15.00%

Entrada
A entrada consiste em vários arquivos de teste, que conterá o valor bruto do salário e adicional dos benefícios. Conforme mostrado no exemplo de entrada a seguir.

Saída
Para cada arquivo da entrada, terá um arquivo de saída. E como mencionado no Desafio, será gerado uma linha com um número que será a diferença entre o valor bruto do salário e o percentual de imposto mediante a faixa salárial somado com o adicional dos benefícios. Use o exemplo abaixo para clarear o que está sendo pedido.

Entrada	Saída
2000 250

Esse é o codigo que eu fiz.

''' 
Para ler e escrever dados em Python, utilizamos as seguintes funções: 
- input: lê UMA linha com dado(s) de Entrada do usuário;
- print: imprime um texto de Saída (Output), pulando linha.  
'''

#Função útil para o calculo do imposto (baseado nas aliquotas).
def calcular_imposto(salario):
  aliquota = 0.00
  if (salario >= 0 and salario <= 1100):
    aliquota = 0.05
  if (salario >= 1101 and salario <= 2500):
    aliquota = 0.10
  if (salario <= 2501):
    aliquota = 0.15
  #TODO Criar as demais condições para as aliquotas de 10.00% e 15.00%.
  return aliquota * salario

#Lê os valores de Entrada:
valor_salario = float(input(2000))
valor_beneficios = float(input(250))

#Calcula o imposto através da função "calcular_imposto":
valor_imposto = calcular_imposto(valor_salario)
#Calcula e imprime a Saída (com 2 casas decimais):
saida = valor_salario - valor_imposto + valor_beneficios
print(f'{saida:.2f}')

Desafio 3
Descrição
Este desafio de código é destinado a profissionais de QA, com o objetivo de explorar a universalidade dos conceitos de qualidade de software através de diversas linguagens de programação. A familiaridade com linguagens específicas é valiosa, mas o foco deve estar nas práticas que garantem a robustez e confiabilidade do código. Aprender diferentes linguagens é um processo natural na carreira de um QA, e este desafio é uma oportunidade para ver como os conceitos de qualidade são aplicados de maneira semelhante em diferentes ambientes de programação.

Dicas importantes:

"A qualidade do software transcende as barreiras da linguagem de programação. Concentre-se em aprender os conceitos fundamentais que são aplicáveis em qualquer linguagem."
"A validação de dados é uma parte essencial do trabalho de QA. Este desafio simula essa responsabilidade de forma prática e educativa."
"Observe e compare como diferentes linguagens alcançam um objetivo comum em termos de qualidade do código. Cada linguagem tem suas peculiaridades, mas os princípios subjacentes de boa programação permanecem os mesmos."
Entrada
A entrada será um texto de três linhas, assuma a premissa de que todas as linhas terão informações/dados:
Nome (string)
Idade (inteiro)
E-mail (string)

Saída
O programa deve validar as informações de entrada seguindo estas regras de negócio:

Dados Válidos: Se todas as informações estiverem corretas:
Dados Validados com Sucesso!
E-mail Inválido: Se o e-mail não possuir os caracteres '@' e '.':
Dados Invalidos: E-mail no formato incorreto!
Idade Inválida: Se a idade não estiver entre 0 e 120 anos:
Dados Invalidos: Idade fora do intervalo permitido!
Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

Entrada	Saída
Alice
30
alice@example.com	Dados Validados com Sucesso!
Bob
150
bob@example.com	Dados Invalidos: Idade fora do intervalo permitido!
Carol
35
carolexample.com	Dados Invalidos: E-mail no formato incorreto!
Eva
Idade: -5
eva@example.com	Dados Invalidos: Idade fora do intervalo permitido!
Frank
45
frank_test@com

Esse eu em tinha feito ainda, mas já coloca pra ficar todos na mesma página.

