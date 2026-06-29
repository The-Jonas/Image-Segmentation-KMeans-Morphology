import cv2
import numpy as np

"""
Operacoes morfologicas e analise de componentes conexos
(itens 5 e 6 do enunciado da Questao 1).
"""

def abertura(img_bin: np.ndarray, tamanho_kernel: int = 3) -> np.ndarray:
    """Remove estruturas finas e ruidos isolados via erosão seguida de dilatação"""
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (tamanho_kernel, tamanho_kernel))
    return cv2.morphologyEx(img_bin, cv2.MORPH_OPEN, kernel)

def fechamento(img_bin: np.ndarray, tamanho_kernel: int = 3) -> np.ndarray:
    """Fecha pequenos buracos dentro das regiões de interesse via dilatação seguida de erosão"""
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (tamanho_kernel, tamanho_kernel))
    return cv2.morphologyEx(img_bin, cv2.MORPH_CLOSE, kernel)

def elementos_conexos(img_bin: np.ndarray):
    """Rotula os componentes conexos da máscara binária e retorna os labels + estatísticas (área, box, centroíde)"""
    _, labels, stats, _ = cv2.connectedComponentsWithStats(img_bin, connectivity=8)
    return labels, stats

def maior_componente(labels: np.ndarray, stats: np.ndarray, criterio: str = "compacidade", area_maxima_fracao: float = None) -> np.ndarray:
    """Seleciona a mascara do componente mais provavel de ser o tumor, por compacidade ou area."""
    indices = np.arange(1, len(stats))
    areas = stats[1:, cv2.CC_STAT_AREA].astype(float)
    larguras = stats[1:, cv2.CC_STAT_WIDTH].astype(float)
    alturas = stats[1:, cv2.CC_STAT_HEIGHT].astype(float)

    if area_maxima_fracao is not None:
        area_total = labels.shape[0] * labels.shape[1]
        validos = areas <= area_maxima_fracao * area_total
        indices, areas, larguras, alturas = (
            indices[validos], areas[validos], larguras[validos], alturas[validos]
        )

    if criterio == "compacidade":
        # razao area/bbox: blobs preenchidos pontuam alto, aneis e linhas finas pontuam baixo
        pontuacao = areas / (larguras * alturas)
    elif criterio == "area":
        pontuacao = areas
    else:
        raise ValueError("criterio deve ser 'compacidade' ou 'area'")

    escolhido = indices[np.argmax(pontuacao)]
    return np.uint8(labels == escolhido) * 255