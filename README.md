
# 🛡️ Sentinel AI: De Gates de Qualidade a LLMs em Containers

### 🔍 A Evolução do Projeto

Este repositório iniciou como um **Gate de Qualidade** (Quality Gate) para validar métricas de performance de modelos. Hoje, ele evoluiu para o **Sentinel AI**: um monitor de mercado inteligente que integra **FastAPI** e **IA Generativa (Llama 3.2)** para transformar dados financeiros brutos em análises técnicas automatizadas.

O objetivo mudou de "validar dados estáticos" para **"gerar insights em tempo real com infraestrutura profissional"**.

---

### 🛠️ Pilares de Engenharia 2.0 (Foco em MLOps)

A arquitetura foi redesenhada seguindo os padrões de mercado para garantir escalabilidade:

1. **Data Ingestion:** Coleta assíncrona de ativos (ex: Ouro) via `yfinance`.
2. **AI Reasoning:** Orquestração do modelo **Llama 3.2** para análise de sentimento e técnica.
3. **Containerization (DevOps):** Todo o ecossistema roda em **Docker**, isolando dependências e garantindo que o código funcione em qualquer ambiente.
4. **Hybrid Networking:** Implementação de ponte de rede (`host-gateway`) para permitir que o container Docker consuma a IA processada pelo hardware local (GPU/CPU via Ollama).
5. **Quality Gate 2.0:** A lógica de validação agora atua no refinamento do prompt e na limpeza de dados da IA.

---

### 💻 Stack Tecnológica

* **Linguagem:** Python 3.11 (Otimizado para FastAPI).
* **Interface:** FastAPI (Documentação automática via Swagger).
* **Inteligência Artificial:** Ollama & Llama 3.2.
* **Infraestrutura:** Docker & Docker Desktop.
* **Dados:** Yahoo Finance API.

---

### 🚀 Como Executar a Nova Versão

A grande evolução é que você não precisa mais instalar bibliotecas manualmente na sua máquina. O **Docker** cuida de tudo:

1. **Construir a Imagem:**
```bash
docker build -t sentinel-ai .

```


2. **Rodar com Integração de IA:**
```bash
docker run -p 8000:8000 --add-host=host.docker.internal:host-gateway sentinel-ai

```


3. **Ver o Resultado:**
Acesse: `http://127.0.0.1:8000/analisar/ouro`

---

### 🧠 Lições de Engenharia (Desafios Superados)

Este projeto reflete a superação de problemas reais de infraestrutura:

* **BIOS e Virtualização:** Configuração de hardware para suporte a Hyper-V e WSL2.
* **Docker Networking:** Resolução de conflitos de `localhost` entre container e host.
* **Data Cleaning:** Tratamento de respostas de LLMs (removendo caracteres especiais e quebras de linha indesejadas).

---

### 📈 Próximos Passos

* [ ] Adicionar suporte a múltiplos ativos simultâneos.
* [ ] Implementar persistência de dados (Banco de Dados no Docker).
* [ ] Criar interface visual (Frontend) para os relatórios.

---

