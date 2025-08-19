class Restaurante:
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False

restaurante_praca = Restaurante("Praça", "Gourmet")
restaurante_pizza = Restaurante("Pizza", "Italiana")

print(vars(restaurante_praca))
print(vars(restaurante_pizza))

restaurantes = [restaurante_praca, restaurante_pizza]

# print(dir(restaurante_praca))