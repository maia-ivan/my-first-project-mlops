# 1. Começamos com uma imagem oficial do Python
FROM python:3.11-slim

# 2. Criamos uma pasta dentro do container para o código
WORKDIR /app

# 3. Copiamos o arquivo de dependências primeiro (otimiza o cache)
COPY requirements.txt .

# 4. Instalamos as bibliotecas dentro do container
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copiamos todo o projeto para dentro do container
COPY . .

# 6. Avisamos que o container vai usar a porta 8000
EXPOSE 8000

# 7. Comando para ligar a API quando o container iniciar
CMD ["python", "-m", "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]