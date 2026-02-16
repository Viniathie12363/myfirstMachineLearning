# 🍎 Classificador de Frutas com Machine Learning

Este é o meu **primeiro projeto** de Machine Learning! O objetivo foi criar um modelo capaz de identificar diferentes tipos de frutas com base em suas características físicas e gustativas.

## 🚀 Sobre o Projeto

O projeto utiliza um algoritmo de **Árvore de Decisão** para classificar frutas. O modelo aprende padrões a partir de um conjunto de dados (`.xlsx`) e, após o treinamento, consegue prever qual é a fruta com base em novas entradas.

### Características analisadas:
* **Arredondada** (Sim/Não)
* **Suculenta** (Sim/Não)
* **Vermelha** (Sim/Não)
* **Doce** (Sim/Não)

## 🛠️ Tecnologias Utilizadas

* **Python 3.x**
* **Pandas**: Para manipulação e leitura dos dados.
* **Scikit-learn**: Para a criação e treinamento do modelo de Machine Learning (`DecisionTreeClassifier`).
* **Matplotlib**: Para a visualização gráfica da árvore de decisão.

## 📊 Como funciona o código

1.  **Carregamento**: O script lê uma base de dados em Excel usando o Pandas.
2.  **Preparação**: Separamos as características (X) do que queremos prever (y - o nome da fruta).
3.  **Treinamento**: O modelo "estuda" os dados para criar regras de decisão.
4.  **Predição**: Testamos o modelo com novos dados para ver se ele acerta a fruta.
5.  **Visualização**: Geramos um gráfico da árvore para entender o raciocínio da IA.

## 📁 Estrutura de Pastas

```text
.
├── data/
│   └── dados_fruta.xlsx    # Base de dados original
├── frutas.py               # Script principal do projeto
└── README.md               # Documentação do projeto
