"""
Autor: Jorge Caetano

Proposito: Fornecer uma classe que simula um caixa eletronico
"""


from collections import OrderedDict


class CaixaEletronico():
    """
    Classe que representa um Caixa Eletronico
    """
    __slots__ = ('notas',)

    def __init__(self):
        self.notas = set()

    def adiciona_nota(self, valor_nota):
        """
        Adiciona notas disponíveis ao caixa eletrônio

        Seguindo a Regra:

        Usuário devera entrar com todas as notas disponíveis 'y', onde 'y' é inteiro e 1 <= y <= 1000.
        Não sera necessário exibir a quantidade de cada nota, pois, como dito na definição do problema as
        notas que forem adicionadas são infinitas, isso é, se a nota de valor 5 esta disponível a mesma
        poderá ser utilizada quantas vezes for necessário para compor um certo valor 'x'.

        :param valor_nota: string - Valor a ser inserido
        :return: Dicionário - contendo 'success' (Sucesso) e 'msg' (mensagem de erro ou de sucesso)
        """
        try:
            i_nota = int(valor_nota)
            valido = (i_nota >= 1) and (i_nota <= 1000)
            if not valido:
                return {'success': False, 'msg': 'O Valor informado [{}] para nota é inválido.'.format(valor_nota)}
            self.notas.add(i_nota)
            return {'success': True, 'msg': 'Nota inserido com sucesso'}
        except:
            return {'success': False, 'msg': 'O Valor informado [{}] para nota é inválido.'.format(valor_nota)}

    def capta_valor(self, valor):
        """
        Responsável por captar o valor que será "sacado"

        Seguindo a Regra:

        Usuario devera entrar com todos os testes 'x', onde 'x' é inteiro e 0 <= z <= 10000.

        :param valor: A ser sacado.
        :return: Dicionário - contendo 'success' (Sucesso) e 'msg' (mensagem de erro ou de sucesso)
        """

        def imprime_notas(notas, valor_imprimir):
            """
            Função que de fato imprime a quantidade de notas necessárias.

            Seguindo a regra

            Apos processar cada teste, o resultado devera ser printado na tela informando quais notas são necessárias e
            qual a quantidade de cada uma sera necessária para compor o valor 'x' digitado pelo usuário, lembrando que
            só poderá utilizar as notas disponíveis na lista de notas validas.

            :param notas: Set - Notas disponíveis
            :param valor_imprimir: inteiro - Valor a ser sacado
            :return:
            """
            if valor_imprimir == 0:
                return False, 'Para valores abaixo de 1 (um) não será possível sacar.'
            _usadas = OrderedDict()
            buffer_notas = notas.copy()
            for num, i in enumerate(sorted(notas, reverse=True)):
                buffer_notas.remove(i)
                if valor_imprimir >= i:
                    while valor_imprimir >= i:
                        qtde = int(valor_imprimir / i)
                        valor_imprimir = (valor_imprimir % i)
                        _usadas[i] = qtde
                        _notas = notas.copy()
                        _notas.remove(i)
                        if valor_imprimir <= 0:
                            break
                        divisivel = imprime_notas(buffer_notas.copy(), valor_imprimir)[0]
                        if not divisivel:
                            valor_imprimir = valor_imprimir + i
                            _usadas[i] = _usadas.get(i, 0) - 1
                            break
                    if valor_imprimir <= 0:
                        break
            if valor_imprimir > 0:
                return False, 'Notas insuficientes para saque do valor solicitado'
            return True, '\n'.join(['{} Nota(s) de {}'.format(v, k) for k, v in _usadas.items() if v > 0])

        try:
            if not self.notas:
                return {'success': False, 'msg': 'Não há notas disponíveis'}
            i_valor = int(valor)
            valido = (i_valor >= 0) and (i_valor <= 1000)
            if not valido:
                return {'success': False, 'msg': 'O Valor informado [{}] é inválido.'.format(valor)}
            success, msg = imprime_notas(self.notas, i_valor)
            return {'success': success, 'msg': msg}
        except Exception as err:
            return {'success': False, 'msg': 'O Valor informado [{}] é inválido.'.format(valor)}


if __name__ == "__main__":
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
        print(res['msg'], '\n')
