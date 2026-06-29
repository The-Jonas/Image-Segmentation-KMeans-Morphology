# Image Segmentation: K-Means & Morphology

**Sobre o Projeto**

Este projeto foi desenvolvido para a disciplina de **Introdução ao Processamento de Imagens (PDI) da Universidade de Brasília (UnB)** e tem como objetivo explorar e implementar duas técnicas clássicas de segmentação de imagens: **morfologia matemática** sobre imagens monocromáticas e **agrupamento não supervisionado (k-means)** sobre o espaço de cor.

O foco é o entendimento algorítmico por trás de cada etapa de um pipeline de segmentação — desde a filtragem de ruído até a discriminação final da estrutura de interesse — avaliando criticamente onde abordagens ingênuas falham e por quê.

🚀 **Exemplos de Aplicação**

* *Detecção de candidato a tumor em exame de tomografia computadorizada (TC) cerebral via filtragem, limiarização de Otsu e morfologia matemática.*
* *Segmentação por cor de uma imagem de hortaliças via k-means, com seleção automática do número de clusters.*
* *Discriminação de estruturas anatômicas (lesão vs. crânio vs. artefatos) através de uma métrica de compacidade geométrica.*
* *Análise crítica do compromisso entre critérios estatísticos (cotovelo, silhueta) e a granularidade semântica desejada na segmentação.*

---

## 📁 Estrutura do Projeto

```text
IMAGE-SEGMENTATION-KMEANS-MORPHOLOGY/
│
├── core/                    # Código-fonte principal com a lógica de processamento
│   ├── io_utils.py          # Leitura/escrita de imagens e conversão para escala de cinza
│   ├── filters.py           # Filtros passa-baixas e de mediana
│   ├── binarization.py      # Histograma e limiarização automática (Otsu)
│   ├── morphology.py        # Abertura, fechamento, componentes conexos e compacidade
│   ├── kmeans_seg.py        # Agrupamento por cor via k-means
│   └── visualization.py     # Funções de plot padronizadas
│
├── data/
│   ├── input/                # brain.jpg, onion.jpg (imagens originais)
│   └── output/q1, q2/        # Resultados gerados pelos notebooks
│
├── notebooks/
│   ├── question_1.ipynb      # Questão 1: candidato a tumor (morfologia)
│   └── question_2.ipynb      # Questão 2: segmentação por cor (k-means)
│
├── report/                   # Relatório técnico em formato IEEE (LaTeX)
│   ├── relatorio.pdf
│   └── figuras/
│
├── requirements.txt          # Dependências do projeto
├── .gitattributes            # Normaliza estatísticas de linguagem do GitHub
└── README.md                 # Este arquivo
```

### 📌 Algoritmos e Conceitos Aplicados:

**Pré-processamento:** Filtro passa-baixas (média), Filtro de mediana, Limiarização automática de Otsu.

**Morfologia Matemática:** Abertura, Fechamento, Componentes Conexos, Métrica de Compacidade (área / bounding box).

**Aprendizado Não Supervisionado:** K-Means, Método do Cotovelo (inércia/WCSS), Coeficiente de Silhueta.

**Avaliação Crítica:** Análise de sensibilidade a hiperparâmetros (tamanho do elemento estruturante, número de clusters) e seus trade-offs.

## ⚙️ Como rodar o projeto

Todo o código foi desenhado para ser autoexplicativo e fácil de executar. A forma recomendada de explorar o projeto é através do Jupyter Notebook, onde todos os passos, imagens e resultados estão comentados e visíveis.

#### *1. Requisitos:*

Python 3.10+   
OpenCV (cv2)   
NumPy   
Matplotlib   
scikit-learn   
Jupyter Notebook   

#### *2. Instalação (Usando Ambiente Virtual):*

Clone o repositório e acesse a pasta do projeto:
```bash
git clone https://github.com/The-Jonas/Image-Segmentation-KMeans-Morphology.git
cd Image-Segmentation-KMeans-Morphology
```

Crie e ative o ambiente virtual (venv):
```bash
# No Windows:
python -m venv .venv
.venv\Scripts\activate

# No Linux/Mac:
python3 -m venv .venv
source .venv/bin/activate
```

Instale as dependências:
```bash
pip install -r requirements.txt
```

#### *3. Execução:*

Para rodar todo o projeto e visualizar as imagens passo a passo, inicie o Jupyter Notebook:
```bash
jupyter notebook
```

**Dica:** Abra os notebooks na pasta `notebooks/` e execute **todas as células em ordem** (`Run All`). Cada notebook importa as funções da pasta `core/`, processa as imagens da pasta `data/input/` e salva os resultados em `data/output/`.

## 🛠️ Funcionalidades e Estrutura do Código

As principais funções estão divididas em módulos na pasta `core/`:

📌 1. `io_utils.py` (Entrada/Saída)
- Carrega imagens do disco, converte para escala de cinza quando necessário e salva resultados intermediários em `data/output/`.

📌 2. `filters.py` (Pré-processamento)
- Aplica filtro passa-baixas (média) seguido de filtro de mediana, reduzindo ruído antes da binarização sem comprometer a textura anatômica relevante.

📌 3. `binarization.py` (Limiarização)
- Calcula o histograma de níveis de cinza e encontra automaticamente o melhor limiar de binarização via método de Otsu.

📌 4. `morphology.py` (Morfologia Matemática)
- Aplica abertura e fechamento para refinar a máscara binarizada, identifica componentes conexos e seleciona o candidato a tumor por meio de uma métrica de **compacidade** (em vez de área bruta, que se mostrou um critério falho nesta aplicação).

📌 5. `kmeans_seg.py` (Segmentação por Cor)
- Agrupa os pixels da imagem por cor via k-means, com escolha automática do número de clusters pelo método do cotovelo, e reconstrói a imagem segmentada.

📌 6. `visualization.py` (Visualização)
- Funções padronizadas de plot (comparação lado a lado, histograma com limiar) usadas em ambos os notebooks.

## 📊 Resultados Principais

- **Questão 1:** o critério ingênuo de "maior componente conexo" falha nesta imagem (seleciona o crânio, não o tumor); a métrica de compacidade resolve isso de forma robusta.
- **Questão 2:** o método do cotovelo selecionou `k=5` automaticamente; análise qualitativa adicional sugere `k=7` como refinamento semântico.
- Discussão completa, com figuras e tabelas, disponível no relatório técnico em [`report`](./report).

