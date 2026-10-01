# 🎲 Bac Bo Simulator

Simulador local desenvolvido em Python para treinamento, estudo de lógica, análise de sequências e gerenciamento de créditos virtuais.

## Importante

Este projeto é exclusivamente educacional.

Não possui integração com:

* Cassinos reais
* Sites de apostas
* APIs externas de apostas
* Depósitos
* Saques
* PIX
* Cartões
* Criptomoedas
* Sistemas de pagamento
* Contas reais
* Dinheiro real

Todos os valores utilizados pelo sistema representam apenas créditos fictícios.

---

# Requisitos

* Python 3.11 ou superior
* VS Code
* Terminal integrado

---

# Estrutura do projeto

```text
bacbo_simulator/
│
├── app.py
├── game.py
├── strategies.py
├── analytics.py
├── bankroll.py
├── requirements.txt
└── README.md
```

---

# Instalação

Abra o VS Code e crie uma pasta chamada:

```text
bacbo_simulator
```

Dentro dela, crie os arquivos:

```text
app.py
game.py
strategies.py
analytics.py
bankroll.py
requirements.txt
README.md
```

Copie o código correspondente para cada arquivo.

---

# Criar ambiente virtual

No terminal do VS Code:

## Windows

```bash
python -m venv .venv
```

Ative:

```bash
.venv\Scripts\activate
```

## Linux / macOS

```bash
python3 -m venv .venv
```

Ative:

```bash
source .venv/bin/activate
```

---

# Instalar dependências

Execute:

```bash
pip install -r requirements.txt
```

---

# Executar o simulador

No terminal:

```bash
streamlit run app.py
```

O Streamlit iniciará um servidor local.

Normalmente o projeto estará disponível em:

```text
http://localhost:8501
```

---

# Funcionalidades

## Sessão virtual

É possível configurar:

* Banca inicial
* Valor da aposta virtual
* Stop Loss
* Stop Win
* Número máximo de rodadas

## Resultados

Cada rodada gera:

* Dois dados para o Player
* Dois dados para o Banker
* Soma de cada lado
* Resultado final

Os resultados possíveis são:

```text
PLAYER
BANKER
EMPATE
```

---

# Histórico visual

O sistema utiliza:

```text
🔴 PLAYER
🔵 BANKER
⚪ EMPATE
```

Exemplo:

```text
🔴 🔴 🔵 🔵 🔴 🔵 🔴
```

---

# Modos de análise

O simulador possui os seguintes modos:

## SURF

Identifica tendências visuais recentes.

## ZIG-ZAG

Analisa alternâncias entre Player e Banker.

Exemplo:

```text
🔴 🔵 🔴 🔵 🔴 🔵
```

## PARES

Analisa possíveis estruturas de dois resultados iguais.

Exemplo:

```text
🔴 🔴 🔵 🔵 🔴 🔴
```

## SEQUÊNCIA

Identifica sequências consecutivas.

Exemplo:

```text
🔵 🔵 🔵 🔵
```

## OBSERVAÇÃO LIVRE

Apresenta apenas o histórico, sem classificar uma estratégia específica.

---

# Dragão

O número mínimo para considerar uma sequência visual como Dragão pode ser configurado na interface.

Exemplo:

```text
🔵 🔵 🔵 🔵 🔵 🔵
```

---

# Quebra de padrão

O sistema também detecta possíveis interrupções de sequências.

Exemplo:

```text
🔴 🔴 🔴 🔴 🔵
```

Nesse caso, o simulador informa que uma possível quebra foi identificada e recomenda observar novas rodadas antes de interpretar uma nova estrutura.

---

# Observação estatística

Os módulos de SURF, sequência, zigue-zague, pares, Dragão e quebra de padrão são ferramentas de análise do histórico.

Eles não garantem:

* O próximo resultado
* Lucro
* Acerto
* Previsão de rodadas futuras

Cada resultado do simulador é gerado aleatoriamente.

O objetivo do projeto é permitir treinamento de:

* Organização de dados
* Programação em Python
* Estatística básica
* Análise de sequências
* Visualização de histórico
* Gerenciamento de créditos fictícios
* Criação de interfaces com Streamlit
