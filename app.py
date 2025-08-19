from modelos.restaurante import Restaurante

restaurante_mexicano = Restaurante('mexicano', 'mexican food')
restaurante_mexicano.receber_avaliacao('John', 10)
restaurante_mexicano.receber_avaliacao('Doe', 8)
restaurante_mexicano.receber_avaliacao('James', 7)

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()