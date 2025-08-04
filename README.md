# Desafio de Programação: Classificação de Pistas de Pouso em Imagens de Satélite

Bem-vindo(a) ao desafio de programação! O objetivo é construir uma aplicação capaz de identificar e classificar pistas de pouso em uma imagem de satélite Sentinel-2, com foco na região do sudoeste paraense. Você tem a liberdade de escolher a abordagem tecnológica, seja utilizando o Google Earth Engine (GEE) para processamento em nuvem ou baixando a imagem para processamento local.

---

## O Desafio

Seu projeto deve abordar os seguintes pontos:

1.  **Acesso à Imagem Sentinel-2:** Obtenha uma imagem de satélite **Sentinel-2** cobrindo a região do **sudoeste paraense**. Você pode definir as coordenadas exatas ou usar um polígono que represente a área de interesse. A coleta dos dados pode ser feita através da API do Google Earth Engine (`ee`), da biblioteca `xee` (uma extensão do GEE para `xarray`) ou por meio de download direto.

2.  **Pré-processamento (Opcional, mas recomendado):** Se achar necessário, aplique técnicas de pré-processamento na imagem para melhorar a qualidade e facilitar a classificação. Isso pode incluir a remoção de nuvens, correção atmosférica (se não estiver pré-aplicada) ou a criação de índices de vegetação.

3.  **Classificação de Pistas de Pouso:** Desenvolva um algoritmo ou modelo para classificar as áreas que correspondem a pistas de pouso na imagem. A escolha da metodologia é sua desde que seja um segmentador semantico como as redes em forma de U ou até mesmo Transformers como o SwinTransformer.

4.  **Visualização e/ou Exportação:** Apresente os resultados da sua classificação de forma clara. Isso pode ser uma visualização interativa (no GEE ou em uma biblioteca como `folium`), ou a exportação dos resultados para um formato geoespacial padrão, como **GeoJSON** ou **GeoTIFF**, com as áreas classificadas.

---

## Requisitos Técnicos

Você pode usar as seguintes ferramentas, mas sinta-se à vontade para explorar outras:

* **Linguagem de Programação:** **Python** é altamente recomendado devido à vasta gama de bibliotecas geoespaciais e de aprendizado de máquina.
* **Acesso a Dados:**
    * **Google Earth Engine (GEE):** Para processamento em nuvem. Use a biblioteca `earthengine-api` ou `xee` para uma interface mais intuitiva.
* **Bibliotecas Sugeridas:**
    * `earthengine-api`
    * `xee` (para integrar o GEE com `xarray`)
    * `rasterio` e `fiona` (para manipulação de dados geoespaciais)
    * `scikit-learn` (para modelos de Machine Learning)
    * `matplotlib` ou `folium` (para visualização)
    * `geopandas` (para análise de dados vetoriais)

---

## Entrega do Projeto

Seu projeto deve ser entregue com os seguintes componentes:

* **Código-fonte:** Todo o código utilizado (scripts Python, notebooks Jupyter, etc.).
* **Instruções de Execução:** Um guia detalhado explicando como configurar o ambiente e executar seu código.
* **Resultados:** Uma amostra dos resultados gerados (imagens, mapas, arquivos). Se a visualização for interativa, inclua uma captura de tela ou um GIF.
* **Documentação:** Um texto breve (pode ser no próprio README) descrevendo a sua abordagem, a metodologia de classificação escolhida, os desafios encontrados e como você os superou.

---

## Critérios de Avaliação

O projeto será avaliado com base em:

* **Funcionalidade:** A aplicação executa as tarefas propostas de forma correta e completa.
* **Qualidade do Código:** Organização, clareza, modularidade e uso de boas práticas de programação.
* **Escolha da Abordagem:** A justificativa para as ferramentas e métodos utilizados é clara e bem fundamentada.
* **Documentação:** As instruções e explicações fornecidas são fáceis de entender.

---

## Como Começar

1. **Faça um fork deste repositório.**

2. **Clone o repositório** para sua máquina local.

3. **Crie um ambiente virtual** (recomendado) e instale as dependências necessárias.

4. **Configure o acesso ao Google Earth Engine** (se for utilizá-lo). Siga as instruções oficiais do GEE para autenticação.

5. **Comece a codificar!**

Boa sorte e divirta-se com o desafio!
