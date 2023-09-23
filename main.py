# Constantes para a altura e largura máximas permitidas
ALTURA = 200
LARGURA = 200


def calcular_novas_dimensoes(largura_original, altura_original, max_pixels=ALTURA * LARGURA):
    """
    Calcula as novas dimensões de uma imagem para que o número total de pixels
    não exceda um valor máximo definido, mantendo o mesmo aspect ratio.

    Parâmetros:
    - largura_original (int): Largura original da imagem.
    - altura_original (int): Altura original da imagem.
    - max_pixels (int): Número máximo de pixels permitidos para a imagem redimensionada.

    Retorna:
    - tuple: Nova largura e nova altura como um tuple de inteiros.
    """
    # Calcular o número total de pixels na imagem original
    pixels_original = largura_original * altura_original

    # Calcular o fator de redimensionamento
    fator_redimensionamento = (max_pixels / pixels_original) ** 0.5

    # Calcular as novas dimensões
    nova_largura = int(largura_original * fator_redimensionamento)
    nova_altura = int(altura_original * fator_redimensionamento)

    return nova_largura, nova_altura


def main():
    """
    Função principal para executar a calculadora de dimensões.
    """
    while True:
        # Definir as dimensões originais da imagem
        largura_original = int(input("Insira a largura original: "))
        altura_original = int(input("Insira a altura original: "))

        # Calculando as novas dimensões
        nova_largura, nova_altura = calcular_novas_dimensoes(largura_original, altura_original)
        print(f"As novas dimensões são: {nova_largura} x {nova_altura}")

        # Perguntar ao usuário se deseja continuar
        resposta = input("Deseja inserir novas dimensões? (s/n): ").strip().lower()
        if resposta == 'n':
            break


if __name__ == "__main__":
    main()
