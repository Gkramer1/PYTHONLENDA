
# importa uma classe de inicial
from inicial import Investimento


class Carteira_investimento:
    def __init__(self, Investimento, quantidade, rentabilidade_mensal, rentabilidade_anual):
        self.Investimento = Investimento
        self.quantidade = quantidade
        self.rentabilidade_mensal = rentabilidade_mensal
        self.rentabilidade_anual = rentabilidade_anual
