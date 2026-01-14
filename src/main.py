from fastapi import FastAPI
import yfinance as yf
import ollama

# 1. Criação da API
app = FastAPI(title="Sentinel AI - Market Monitor")

# 2. CONFIGURAÇÃO DO CLIENTE (O segredo para o Docker ver o Windows)
# O endereço 'host.docker.internal' permite que o container acesse o Ollama no seu PC
client = ollama.Client(host='http://host.docker.internal:11434')

@app.get("/")
def home():
    return {"status": "online", "engine": "Llama 3.2 (via Docker)"}

@app.get("/analisar/ouro")
def analisar_ouro():
    # Coleta de dados do Yahoo Finance
    gold = yf.Ticker("GC=F")
    historico = gold.history(period="5d")
    preco_atual = round(historico['Close'].iloc[-1], 2)
    
    # Prompt para a IA
    prompt = (
        f"O preço atual do ouro (GC=F) é USD {preco_atual}. "
        f"Analise os últimos 5 dias e escreva um parágrafo curto começando com: "
        f"'O preço atual é {preco_atual}...' e dê sua visão técnica."
    )
    
    # Chamada usando o 'client' configurado acima
    response = client.chat(model='llama3.2', messages=[
        {'role': 'user', 'content': prompt}
    ])
    
    return {
        "ativo": "Ouro",
        "preco": preco_atual,
        "analise_ia": response['message']['content']
    }
    