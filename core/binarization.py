import cv2
import numpy as np

"""
Analise de histograma e binarizacao (item 4 do enunciado da Questao 1).
"""

def calcular_histograma(img: np.ndarray) -> np.ndarray:
    """Calcula o histograma de níveis de cinza da imagem (256 bins)"""
    return cv2.calcHist([img], [0], None, [256], [0, 256]).flatten()

def encontrar_limiar_otsu(img: np.ndarray) -> int:
    """Encontrar o limiar ótimo de binarização pelo método de Otsu, a partir do histograma."""
    limiar, _ = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return int(limiar)

def binarizar(img: np.ndarray, limiar: int) -> np.ndarray:
    """Binariza a imagem: pixels >= limiar tornam-se 255, os demais 0."""
    _, img_bin = cv2.threshold(img, limiar, 255, cv2.THRESH_BINARY)
    return img_bin