import cv2
import numpy as np

"""
Filtros de suavizacao usados na Questao 1 (item 3 do enunciado):
primeiro um filtro passa-baixas, depois um filtro de mediana, para
remover ruido antes da binarizacao.
"""


def filtro_passa_baixas(img: np.ndarray, tamanho_kernel: int = 5) -> np.ndarray:
    """
    Suaviza a imagem com um filtro de media (passa-baixas), atenuando
    ruido de alta frequencia.

    Parametros
    ----------
    img : np.ndarray
        Imagem monocromatica de entrada.
    tamanho_kernel : int
        Tamanho do kernel (deve ser impar).

    Retorna
    -------
    np.ndarray
        Imagem suavizada, mesmo shape de entrada.
    """
    return cv2.blur(img, (tamanho_kernel, tamanho_kernel))


def filtro_mediana(img: np.ndarray, tamanho_kernel: int = 3) -> np.ndarray:
    """
    Aplica filtro de mediana, removendo ruido impulsivo ("sal e pimenta")
    sem borrar bordas tanto quanto um filtro de media.
    """
    return cv2.medianBlur(img, tamanho_kernel)