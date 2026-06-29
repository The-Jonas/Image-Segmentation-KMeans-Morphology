import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

"""Especificamente funções para a questão 2, utilizando algoritmo k-means"""

def preparar_dados_kmeans(img: np.ndarray) -> np.ndarray:
    """Reorganiza a imagem (H, W, 3) em uma matriz (H*W, 3) de amostras de cor para o KMeans."""
    return img.reshape(-1, 3).astype(np.float32)

def escolher_melhor_k(dados: np.ndarray, k_min: int = 2, k_max: int = 10, metodo: str = "elbow") -> int:
    """Varre k_min..k_man e escolhe o k que melhor segmenta por cor, via cotovelo (inércia) ou silhueta"""
    valores_k = list(range(k_min, k_max + 1))
    
    if metodo == "elbow":
        inercias = [
            KMeans(n_clusters=k, n_init=10, random_state=42).fit(dados).inertia_
            for k in valores_k
        ]
        return _ponto_do_cotovelo(valores_k, inercias)

    if metodo == "silhouette":
        pontuacoes = []
        for k in valores_k:
            labels = KMeans(n_clusters=k, n_init=10, random_state=42).fit(dados).labels_
            pontuacoes.append(silhouette_score(dados, labels, sample_size=2000, random_state=42))
        return valores_k[int(np.argmax(pontuacoes))]
    
    raise ValueError("metodo deve ser 'elbow' ou 'silhouette'")

def _ponto_do_cotovelo(valores_k: list, inercias: list) -> int:
    """Acha o 'cotovelo' da curva de inércia: o ponto mais distante da linha entre o primeiro e o último ponto."""
    pontos = np.array(list(zip(valores_k, inercias)), dtype=float)
    inicio, fim = pontos[0], pontos[-1]
    direcao = (fim - inicio) / np.linalg.norm(fim - inicio)
    distancias = [np.linalg.norm((p - inicio) - np.dot(p - inicio, direcao) * direcao) for p in pontos]
    return int(valores_k[int(np.argmax(distancias))])

def segmentar_kmeans(img: np.ndarray, k: int) -> np.ndarray:
    """Roda o KMeans com k clusters e reconstrói a imagem trocando cada pixel pela cor média do seu cluster"""
    dados = preparar_dados_kmeans(img)
    km = KMeans(n_clusters=k, n_init=10, random_state=42).fit(dados)
    cores_segmentadas = km.cluster_centers_[km.labels_]
    return cores_segmentadas.reshape(img.shape).astype(np.uint8)

