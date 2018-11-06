# caixa_eletronico
Caixa Eletronico

Projeto que representa um caixa eletrônico para saque de valores.

Este projeto contêm a classe CaixaEletronico, com os métodos: adiciona_nota e capta_valor.

Para rodar o caixa eletrônico, basta rodar o módulo "caixa_eletronico.py".

Mas se prefirar utilizar a classe de forma isolada, segue exemplo de uso: 

"""
caixa = CaixaEletronico()

while True:
    nota = input('Por favor. Informe a nota disponível. [Digite -1 para encerrar]')
    if nota == '-1':
        break
    res = caixa.adiciona_nota(nota)
    if not res['success']:
        print(res['msg'])

while True:
    valor = input('Por favor. Informe o valor. [Digite -1 para encerrar]')

    if valor == '-1':
        break
    res = caixa.capta_valor(valor)
    print(res['msg'])
"""
