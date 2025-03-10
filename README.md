# 📌 Calculadora de INSS e IRRF

Este projeto é uma aplicação interativa desenvolvida em **Python** utilizando a biblioteca **Flet**, que permite calcular os descontos de **INSS e IRRF** sobre um salário bruto informado pelo usuário.

## 📌 Funcionalidades
- Entrada do **salário bruto**
- Seleção do **número de dependentes**
- Opção de aplicar o **desconto simplificado** no cálculo do IRRF
- Cálculo automático de **INSS, IRRF e salário líquido**
- Exibição detalhada da **memória de cálculo**

## 🚀 Como Executar no WSL com Poetry
1. **Instale o Poetry** (caso ainda não tenha):
   ```bash
   curl -sSL https://install.python-poetry.org | python3 -
   ```
2. **Clone ou baixe este repositório**
   ```bash
   git clone https://github.com/seu-usuario/calculadora-inss-irrf.git
   cd calculadora-inss-irrf
   ```
3. **Instale as dependências com Poetry**
   ```bash
   poetry install
   ```
4. **Ative o ambiente virtual do Poetry**
   ```bash
   poetry shell
   ```
5. **Execute o aplicativo**
   ```bash
   python main.py
   ```
6. **A interface abrirá automaticamente no navegador**.

## 📌 Estrutura do Projeto
A estrutura do projeto segue a seguinte organização:

```
calculadora_clt/
│── .venv/                   # Ambiente virtual gerenciado pelo Poetry
│── .gitignore               # Arquivo de exclusão do Git
│── .pre-commit-config.yaml  # Configuração para pre-commit hooks
│── main.py                  # Código principal da aplicação
│── poetry.lock              # Lockfile do Poetry para dependências
│── pyproject.toml           # Configuração do projeto e dependências
│── README.md                # Documentação do projeto
```

## 📌 Tecnologias Utilizadas
- **Python 3.11**
- **Flet** (para a interface gráfica)
- **Poetry** (gerenciador de pacotes)
- **WSL (Windows Subsystem for Linux)**

## 📌 Exemplo de Uso
1. Insira o **salário bruto** (exemplo: `5.000,00`).
2. Informe o número de **dependentes** (exemplo: `2`).
3. Escolha se deseja aplicar o **desconto simplificado**.
4. Clique no botão **"Calcular"**.
5. O sistema exibirá:
   - **INSS** calculado
   - **Base do IRRF**
   - **Valor do IRRF**
   - **Salário Líquido**
   - **Memória de Cálculo detalhada**


---
👨‍💻 Desenvolvido por [Edvaldo Gutierres](https://github.com/edvaldo-gutierres)

