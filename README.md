# Projeto RPA — Automação estratégica em Gestão de Dados: Otimização de tempo e excelência operacional

> Repositório com um mini-projeto de RPA (Robotic Process Automation) criado como exemplo para o Trabalho de Conclusão de Curso (TCC): "Automação estratégica em Gestão de Dados: Otimização de tempo e excelência operacional". O objetivo deste projeto é demonstrar, de forma pratica a aplicação de RPA no desempenho específico de atividades relacionadas ao papel do profissional Gestor de Dados.

---

## Conteúdo deste repositório

- `src/` — Código-fonte do robô (scripts, workflows).
- `src/core` - Classes responsáveis por executar uma tarefa específica de RPA.
- `src/utils` - Utilitários utilizados por outras partes do código.
- `src/main.py` - O ponto de entrada para execução principal do projeto.
- `README.md` — Este arquivo.

> Observação: Este projeto utiliza como gerenciador de bibliotecas e projetos Python a ferramenta UV, disponível em: https://docs.astral.sh/uv/getting-started/installation/

## Conteúdo gerado automaticamente (UV):

- `uv.lock` - Arquivo de lock (bloqueio) multiplataforma que contém as versões exatas e resolvidas de todas as dependências do projeto Python (incluindo subdependências).
- `pyproject.toml` - arquivo de configuração baseado no formato TOML (Tom's Obvious, Minimal Language), que serve como um manifesto centralizado para metadados e configurações de ferramentas de um projeto Python (parcialmente gerenciado pelo UV, e parcialmente editado manualmente).
- `python-version` - Arquivo de metadados que informa qual versão do interpretador Python foi usada para o projeto.

---

## Tecnologias e ferramentas sugeridas

> Caso utilize UV como sugerido, todo o ambiente do projeto pode ser rapidamente reproduzido com o comando `uv sync`.

- Python 3.10+
- Bibliotecas: `file-picker-py>=0.2.0`, `openpyxl>=3.1.5`, `pandas>=2.3.3`.
- Ambiente virtual: `uv` ou outro de preferência.
- Ferramentas adicionais (opcional): Git.

---

## Pré-requisitos

1. Ter Python instalado (3.10+. Recomendado >= 3.14).
2. Criar e ativar um ambiente virtual:

## Como executar

Baixe manualmente a partir do repositório, ou via git clone (estando em ambiente de terminal):

```
git clone https://github.com/francisN7/RPA.git
```
Após entre no diretório correto:
```
cd RPA
```

#### Criando e sicronizando um novo ambiente virtual com as configurações e dependências do projeto.

Seguindo a sugestão de utilizar UV:

```
uv sync
```

Após, estando com terminal aberto no diretório do projeto:

```
uv run ./src/rpa/main.py
```

> Caso opte por utilizar outro gerenciador de projetos, os passos de sicronização, instalação e ativação do ambiente virtual podem ser diferentes.

---

## Arquitetura e fluxo do robô

1. **Menu** — Escolha da rotina desejada.
2. **Input** — Seleção dos arquivos a serem processados.
3. **Ação** — O código executa a rotina selecionada anteriormente.
4. **Output** — Arquivos gerados, e salvos.
