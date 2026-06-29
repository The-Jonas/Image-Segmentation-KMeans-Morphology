# Detecção de Tumor via Morfologia Matemática e Segmentação por Cor com K-Means

Projeto II da disciplina de Introdução ao Processamento de Imagens (UnB).

- **Questão 1**: identificação de um candidato a tumor em uma TC cerebral via filtragem, limiarização de Otsu e morfologia matemática.
- **Questão 2**: segmentação por cor de uma imagem de hortaliças via k-means.

## Estrutura do projeto

```
.
├── core/                   # módulos com a lógica de processamento
│   ├── io_utils.py
│   ├── filters.py
│   ├── binarization.py
│   ├── morphology.py
│   ├── kmeans_seg.py
│   └── visualization.py
├── data/
│   ├── input/              # brain.jpg, onion.jpg
│   └── output/q1, q2/      # resultados gerados pelos notebooks
├── notebooks/
│   ├── question_1.ipynb
│   └── question_2.ipynb
├── report/                 # relatório em formato IEEE (LaTeX)
└── requirements.txt
```

## Como executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/The-Jonas/Image-Segmentation-KMeans-Morphology.git
   cd Image-Segmentation-KMeans-Morphology
   ```

2. (Recomendado) Crie um ambiente virtual:
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # Windows: .venv\Scripts\activate
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Abra o Jupyter e execute os notebooks **em ordem, do início ao fim** (Run All Cells):
   ```bash
   jupyter notebook
   ```
   - `notebooks/question_1.ipynb` → Questão 1 (morfologia matemática)
   - `notebooks/question_2.ipynb` → Questão 2 (k-means)

Os resultados (imagens gerados) são salvos automaticamente em `data/output/q1` e `data/output/q2`.

## Relatório

O relatório técnico em formato IEEE está em `report/relatorio.tex`, junto com as figuras usadas (`report/figuras/`). 
