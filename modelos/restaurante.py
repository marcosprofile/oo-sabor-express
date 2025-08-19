class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self._ativo = False
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self.nome} | {self.categoria}'

    def listar_restaurantes():
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome.ljust(20)} | {restaurante.categoria.ljust(20)} | {restaurante.ativo}')

    @property
    def ativo(self):
        return '✅ Ativo' if self._ativo else '⛔ Inativo'

restaurante_praca = Restaurante("Praça", "Gourmet")
restaurante_pizza = Restaurante("Pizza", "Italiana")

print(f'{'Nome do restaurante'.ljust(20)} | {'Categoria'.ljust(20)} | {'Status'}')
Restaurante.listar_restaurantes()