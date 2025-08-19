from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_mexicano = Restaurante('mexicano', 'mexican food')
bebida_suco = Bebida('suco de melancia', 5.0, 'grande')
bebida_suco.aplicar_desconto()
prato_paozinho = Prato('paozinho', 2.0, 'o melhor pão da cidade')
prato_paozinho.aplicar_desconto()

restaurante_mexicano.adicionar_no_cardapio(bebida_suco)
restaurante_mexicano.adicionar_no_cardapio(prato_paozinho)

def main():
    restaurante_mexicano.exibir_cardapio

if __name__ == '__main__':
    main()