"""
Funcoes de visualizacao padronizadas, para manter os notebooks limpos
e os resultados faceis de exportar para o relatorio (dados/saida/).
"""

import cv2
import matplotlib.pyplot as plt
import numpy as np

def mostrar_lado_a_lado(imagens: list, titulos: list, cmap: str = "gray") -> None:
    """Mostra uma lista de imagens lado a lado em uma unica figura, para comparar etapas do pipeline."""
    n = len(imagens)
    fig, eixos = plt.subplots(1, n, figsize=(5 * n, 5))
    if n == 1:
        eixos = [eixos]
    for eixo, img, titulo in zip(eixos, imagens, titulos):
        if img.ndim == 3:
            # cv2 carrega em BGR; matplotlib espera RGB
            eixo.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        else:
            eixo.imshow(img, cmap=cmap)
        eixo.set_title(titulo)
        eixo.axis("off")
    plt.tight_layout()
    plt.show()


def mostrar_histograma(img: np.ndarray, limiar: int = None) -> None:
    """Plota o histograma de niveis de cinza da imagem, com uma linha vertical opcional no limiar escolhido."""
    plt.figure(figsize=(6, 4))
    plt.hist(img.ravel(), bins=256, range=(0, 256), color="gray")
    if limiar is not None:
        plt.axvline(limiar, color="red", linestyle="--", label=f"limiar = {limiar}")
        plt.legend()
    plt.xlabel("Nivel de cinza")
    plt.ylabel("Frequencia")
    plt.title("Histograma")
    plt.show()
    