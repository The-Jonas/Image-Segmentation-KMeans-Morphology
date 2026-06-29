import cv2
import numpy as np
import os

"""
Utilitarios de entrada/saida de imagens.
"""

def carregar_imagem(caminho: str, escala_cinza: bool = False) -> np.ndarray:
    """
    Carrega uma imagem do disco.

    Parametros
    ----------
    caminho : str
        Caminho para o arquivo de imagem (ex: 'dados/entrada/brain.jpg').
    escala_cinza : bool
        Se True, retorna a imagem ja convertida para escala de cinza.

    Retorna
    -------
    np.ndarray
        Imagem carregada: shape (H, W) se escala_cinza=True,
        ou (H, W, 3) caso contrario.
    """
    flag = cv2.IMREAD_GRAYSCALE if escala_cinza else cv2.IMREAD_COLOR
    img = cv2.imread(caminho, flag)
    if img is None:
        raise FileNotFoundError(f"Nao consegui abrir a imagem em: {caminho}")
    return img

def para_escala_cinza(img: np.ndarray) -> np.ndarray:
    """
    Converte uma imagem colorida (H, W, 3) para escala de cinza (H, W).
    Se a imagem ja for monocromatica, retorna sem alteracoes
    """
    if img.ndim == 2:
        return img  # ja e monocromatica
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


def salvar_imagem(caminho: str, img: np.ndarray) -> None:
    """
    Salva uma imagem em disco, criando os diretorios intermediarios se
    necessario. Usado para registrar resultados parciais em dados/saida/.
    """
    pasta = os.path.dirname(caminho)
    if pasta:
        os.makedirs(pasta, exist_ok=True)
    cv2.imwrite(caminho, img)
    