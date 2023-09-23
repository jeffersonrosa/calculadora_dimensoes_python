import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.patches as patches

MAX_LARGURA = 200
MAX_ALTURA = 200


def calcular_dimensoes_novas(largura, altura):
    """
    Calcula as novas dimensões de uma imagem para que o número total de pixels
    não exceda os valores máximos definidos, mantendo o mesmo aspect ratio.

    Parâmetros:
    - largura (int): Largura original da imagem.
    - altura (int): Altura original da imagem.

    Retorna:
    - tuple: Nova largura e nova altura como um tuple de inteiros.
    """
    pixels_originais = largura * altura
    fator_redimensionamento = min(MAX_LARGURA / largura, MAX_ALTURA / altura)
    nova_largura = int(largura * fator_redimensionamento)
    nova_altura = int(altura * fator_redimensionamento)
    return nova_largura, nova_altura


def plotar_dimensoes(largura, altura, nova_largura, nova_altura):
    """
    Plota um gráfico comparando as dimensões originais e as novas dimensões.

    Parâmetros:
    - largura (int): Largura original da imagem.
    - altura (int): Altura original da imagem.
    - nova_largura (int): Nova largura calculada.
    - nova_altura (int): Nova altura calculada.
    """
    fig = Figure(figsize=(5, 4))
    ax = fig.add_subplot(1, 1, 1)

    rect_original = patches.Rectangle((0, 0), largura, altura, fill=None, edgecolor='r', label='Original')
    rect_novo = patches.Rectangle((0, 0), nova_largura, nova_altura, fill=None, edgecolor='b', label='Novo')

    ax.add_patch(rect_original)
    ax.add_patch(rect_novo)

    ax.legend()
    ax.set_xlabel('Largura')
    ax.set_ylabel('Altura')
    ax.set_title('Comparação de Dimensões')
    ax.set_aspect('equal')
    ax.set_xlim(0, max(largura, nova_largura) + 10)
    ax.set_ylim(0, max(altura, nova_altura) + 10)

    ax.text(largura / 2, altura / 2, f'{largura}x{altura}', color='red', ha='center', va='center', fontsize=9,
            bbox=dict(facecolor='white', alpha=0.5, edgecolor='white'))
    ax.text(nova_largura / 2, nova_altura / 2, f'{nova_largura}x{nova_altura}', color='blue', ha='center', va='center',
            fontsize=9, bbox=dict(facecolor='white', alpha=0.5, edgecolor='white'))

    return fig


def calcular_dimensoes_interface():
    try:
        largura = int(entrada_largura.get())
        altura = int(entrada_altura.get())
        nova_largura, nova_altura = calcular_dimensoes_novas(largura, altura)
        fig = plotar_dimensoes(largura, altura, nova_largura, nova_altura)

        canvas = FigureCanvasTkAgg(fig, master=janela_principal)
        widget_canvas = canvas.get_tk_widget()
        widget_canvas.grid(row=3, column=0, columnspan=2)
    except ValueError:
        tk.messagebox.showerror("Entrada Inválida", "Por favor, insira valores válidos para largura e altura.")


def configurar_interface():
    """
    Configura a interface gráfica do programa.
    """
    janela_principal.title("Calculadora de Dimensões")

    tk.Label(janela_principal, text="Largura Original:").grid(row=0, column=0, padx=20, pady=5, sticky="e")
    tk.Label(janela_principal, text="Altura Original:").grid(row=1, column=0, padx=20, pady=5, sticky="e")

    entrada_largura.grid(row=0, column=1, padx=20, pady=5)
    entrada_altura.grid(row=1, column=1, padx=20, pady=5)

    tk.Button(janela_principal, text="Calcular", command=calcular_dimensoes_interface).grid(row=2, column=0,
                                                                                            columnspan=2, pady=10)


if __name__ == "__main__":
    janela_principal = tk.Tk()
    entrada_largura = tk.Entry(janela_principal)
    entrada_altura = tk.Entry(janela_principal)
    configurar_interface()
    janela_principal.mainloop()
