from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('praça', 'gourmet')
restaurante_pizza = Restaurante('pizza', 'italizana')
restaurante_mexicano = Restaurante('mexicano', 'mexican food')
restaurante_mexicano.alternar_estado()

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()