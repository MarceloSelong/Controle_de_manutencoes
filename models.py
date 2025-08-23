class Veiculo:
    def __init__(self, placa, modelo, marca, ano):
        self.__placa = placa
        self.modelo = modelo
        self.marca = marca
        self.ano = ano
        self._lista_de_manutencoes = []

    def para_dict(self):
        return {
            "placa": self.__placa,
            "modelo": self.modelo,
            "marca": self.marca,
            "ano": self.ano,
            "lista_de_manutencoes": self._lista_de_manutencoes
        }

    def adicionar_manutencao(self, manutencao):
        self._lista_de_manutencoes.append(manutencao)

class Servico:
    def __init__(self, descricao, custo , data, quilometragem, lista_de_pecas):
        self.descricao = descricao
        self._custo = custo
        self._data = data
        self._quilometragem = quilometragem        
        self._lista_de_pecas = lista_de_pecas

    def para_dict(self):
        return {
            "descricao": self.descricao,
            "custo": self._custo,
            "data": self._data,
            "quilometragem": self._quilometragem,
            "lista_de_pecas": self._lista_de_pecas
        }



class Pecas:
    def __init__(self, descricao, custo):
        self.descricao = descricao
        self._custo = custo

    def para_dict(self):
        return {
            "descricao": self.descricao,
            "custo": self._custo
        }