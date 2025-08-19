from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_mexicano = Restaurante('mexicano', 'mexican food')
bebida_suco = Bebida('suco de melancia', 5.0, 'grande')
prato_paozinho = Prato('paozinho', 2.0, 'o melhor pão da cidade')

def main():
    print(bebida_suco)
    print(prato_paozinho)

if __name__ == '__main__':
    main()