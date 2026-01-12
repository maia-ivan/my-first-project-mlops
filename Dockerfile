FROM python:3.9-slim

WORKDIR /app

# Copia os requisitos
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia a pasta src e cria a logs
COPY src/ ./src/
RUN mkdir logs

# Comando para rodar apontando para a pasta src
CMD ["python", "src/market_data_validator.py"]