# 🚀 Projeto 01: Gate de Qualidade para MLOps

### 🔍 O que este projeto faz?
Este é o primeiro pilar da minha jornada em Engenharia de MLOps. O objetivo aqui é criar uma camada de segurança (**Gate de Qualidade**) que valida os dados de entrada antes que eles cheguem ao modelo de Inteligência Artificial.

Na engenharia de dados, chamamos isso de prevenção de "Garbage In, Garbage Out" (Lixo entra, Lixo sai).

---

### 🛠️ Pilares de Engenharia Aplicados
Utilizei o checklist de 4 pilares para estruturar o desenvolvimento:

1. **Entrada (Input):** Leitura de métricas de performance de modelos via arquivos CSV.
2. **Processamento (Lógica):** Implementação de regras de negócio para validar `Loss` e `Acurácia`.
3. **Saída (Output):** Veredito automático de aprovação ou rejeição do modelo para produção.
4. **Gestão (Infra):** Versionamento completo do código e histórico de mudanças usando **Git e GitHub**.

---

### 💻 Tecnologias Utilizadas
* **Python 3.x**: Linguagem base para processamento lógico.
* **Pandas**: Biblioteca para manipulação e análise de dados.
* **Git**: Controle de versão e rastreabilidade de código.

---

## 🛠️ Stack Tecnológica
- **Linguagem:** Python 3.10
- **Dados:** yfinance & Pandas
- **CI/CD:** GitHub Actions
- **Containerização:** Docker
- **Infraestrutura:** Terraform (IaC)

---


### 🚀 Como executar o projeto
1. Clone o repositório:
   ```bash
   git clone [https://github.com/maia-ivan/my-first-project-mlops.git](https://github.com/maia-ivan/my-first-project-mlops.git)


   -

Instale as dependências:

Bash

pip install pandas


-

Execute o validador:

Bash

python analise_qualidade.py
