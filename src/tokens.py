
class Token:
    def __init__(self, tipo, valor):
        self.tipo = tipo
        self.valor = valor

    def __repr__(self) -> str:
        return f'{self.tipo}:[{self.valor}]'