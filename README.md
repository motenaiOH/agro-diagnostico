# Sistema de Diagnóstico de Perdas na Colheita de Cana

## 📌 Problema

As perdas na colheita mecanizada da cana-de-açúcar podem chegar a 15% da produção, gerando prejuízos milionários ao produtor rural.

## 🌟 Solução

Este projeto tem como objetivo realizar diagnósticos automatizados de perdas na colheita de cana-de-açúcar, com base em parâmetros operacionais como velocidade, rotação, umidade e temperatura. Os resultados são armazenados e visualizados em tempo real através de um dashboard interativo com Streamlit.

Os limiares e pesos usados no cálculo são carregados dinamicamente a partir de um arquivo externo `parametros_diagnostico.json`, permitindo ajustes fáceis sem alterar o código.

---

## 📂 Estrutura do Projeto

```
agro-diagnostico/
├── app/                      # Aplicação principal
│   ├── main.py              # Menu e execução do diagnóstico
│   ├── diagnostico.py       # Lógica de avaliação
│   ├── relatorio.py         # Geração de relatório JSON
│   ├── db.py                # Simulação de armazenamento
│   └── parametros_diagnostico.json # Parâmetros customizáveis
│
├── dashboard/               # Visualização dos diagnósticos
│   └── dashboard.py         # Painel interativo com filtros e gráficos
│
├── relatorios/              # Saída dos relatórios gerados
│   └── .gitkeep             # Garante que o diretório seja versionado
│
├── scripts/                 # Scripts auxiliares
│   ├── setup.sh             # Instala dependências e executa aplicação (Linux/macOS)
│   └── setup.bat            # Instala e executa aplicação (Windows)
│
├── tests/                   # Testes unitários com pytest
│   ├── test_diagnostico.py
│   ├── test_relatorio.py
│   └── __init__.py
│
├── requirements.txt         # Dependências Python
├── .gitignore               # Regras para versionamento
└── README.md                # Você está aqui
```

---

## ▶️ Como executar

1. Clone o repositório ou descompacte o `.zip`
2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Execute a aplicação:

```bash
cd app
python main.py
```

A aplicação abrirá um menu no terminal e o dashboard será carregado automaticamente no navegador.

---

## ✅ Como executar os testes

A partir da raiz do projeto, rode:

```bash
pytest tests/
```

Certifique-se de que as dependências estão instaladas (especialmente `pytest`). Os testes validam a lógica de diagnóstico e geração de relatórios.

---

## 📊 Funcionalidades

- Diagnóstico baseado em múltiplos parâmetros operacionais
- Geração de relatórios `.json`
- Dashboard com gráficos interativos (Plotly + Streamlit)
- Atualização automática ao gerar novos diagnósticos
- Personalização de regras no arquivo `parametros_diagnostico.json`

---

## 🚧 Em desenvolvimento

- Integração com banco de dados Oracle
- Exportação de relatórios em CSV/XLSX
- Autenticação no dashboard
