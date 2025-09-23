# 🌍 Semantic Segmentation – Projeto de Detecção em Imagens de Satélite

Este projeto implementa um pipeline completo para **segmentação semântica** utilizando imagens de satélite (Sentinel-2).  
O objetivo é identificar e separar diferentes regiões de interesse em imagens geoespaciais, aplicando **Deep Learning** (U-Net) e ferramentas de visualização e monitoramento de métricas.

---

## 📂 Estrutura do Projeto

```
initial-challenge-semantic-segmentation/
│
├─ data/                     # Pasta de dados (imagens .tif, máscaras, etc.)
├─ checkpoints/               # Modelos treinados (.pth)
├─ src/                       # Código-fonte principal
│   ├─ train.py               # Treinamento do modelo
│   ├─ infer.py               # Inferência e geração de previsões
│   ├─ explain.py             # Interpretação com Grad-CAM
│   ├─ metrics.py             # Funções de avaliação
│   ├─ utils.py               # Funções auxiliares (pré-processamento, etc.)
│   └─ models.py              # Definição da arquitetura U-Net
├─ requirements.txt           # Dependências do projeto
└─ README.md                  # Este arquivo
```

---

## 🚀 Fluxo do Projeto

### 1️⃣ **Pré-processamento dos Dados**
As imagens de satélite (GeoTIFF) são carregadas com **Rasterio**, normalizadas e organizadas em tensores PyTorch.  
Isso garante que o modelo receba dados padronizados para aprendizado.

### 2️⃣ **Modelo – U-Net**
- A arquitetura escolhida é a **U-Net**, amplamente usada em segmentação de imagens.  
- Ela possui um **encoder** (extrai características) e um **decoder** (reconstrói a máscara pixel a pixel).

O modelo é definido em `models.py` e pode ser facilmente ajustado para outros datasets ou camadas.

### 3️⃣ **Treinamento (`train.py`)**
- O treinamento utiliza **PyTorch** para otimização.  
- As métricas de desempenho, como **IoU** e **F1-Score**, são calculadas em cada época.  
- A integração com **Weights & Biases (wandb)** registra:
  - Gráficos de perda (loss)
  - Métricas de validação
  - Checkpoints do modelo

Isso permite acompanhar o aprendizado em tempo real e comparar diferentes execuções.

### 4️⃣ **Inferência (`infer.py`)**
- Carrega o modelo treinado (checkpoint `.pth`) e aplica em novas imagens.
- Gera máscaras segmentadas salvas como imagens ou arquivos GeoTIFF.

### 5️⃣ **Interpretação com Grad-CAM (`explain.py`)**
Para entender **quais regiões da imagem influenciam mais as previsões**, usamos o **Grad-CAM**:
- Destaca áreas críticas para a decisão da rede.
- Gera um overlay (heatmap) sobre a imagem original.
- Facilita a análise e explicação do modelo, aumentando a transparência.

---

## 🛠️ Principais Tecnologias
- **PyTorch** – Treinamento e inferência da rede neural.
- **Rasterio** – Leitura de imagens geoespaciais.
- **Weights & Biases (wandb)** – Monitoramento de métricas.
- **Grad-CAM** – Interpretação visual.

---

## 💡 Possíveis Extensões
- **Augmentations** (aumentos de dados) para melhorar a robustez.
- Testes com outras arquiteturas (DeepLab, UNet++).  
- Geração de dashboards interativos com **Streamlit** ou **Dash**.

---

## ⚡ Como Rodar

1️⃣ Instale as dependências:
```bash
pip install -r requirements.txt
```

2️⃣ Treine o modelo:
```bash
python src/train.py
```

3️⃣ Faça a inferência:
```bash
python src/infer.py
```

4️⃣ Gere visualizações Grad-CAM:
```bash
python src/explain.py
```

---

## 📊 Resultado Esperado
Ao final, você terá:
- **Modelo treinado** para segmentação.
- **Máscaras preditas** em novas imagens.
- **Visualizações interpretáveis** (Grad-CAM).
- Histórico de treinamento registrado no **wandb**.

---

🔎 **Resumo Rápido**:  
Este projeto demonstra um pipeline moderno de **Deep Learning aplicado a geoinformação**, com:
- Treinamento de uma rede U-Net em imagens de satélite.
- Avaliação quantitativa (métricas).
- Visualização interpretável (Grad-CAM).
- Registro de experimentos em tempo real.

