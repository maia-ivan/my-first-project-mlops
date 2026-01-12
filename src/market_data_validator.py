import yfinance as yf
import pandas as pd
import logging
import os
import ollama  # Importa a biblioteca da IA

# 1. CONFIGURAÇÃO DE PASTAS E LOGS
# Garante que a pasta de logs exista para não dar erro
os.makedirs('logs', exist_ok=True)

logging.basicConfig(
    filename='logs/gate_gold_history.log', 
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def pedir_analise_ia(media, volatilidade, variacao):
    """Envia os dados para o Llama 3.2 analisar localmente"""
    prompt = f"""
    Como um analista financeiro sênior, analise estes dados do Ouro:
    - Média (5 dias): {media:.2f}
    - Volatilidade (Desvio Padrão): {volatilidade:.2f}
    - Variação Diária: {variacao:+.2f}%
    
    Dê um resumo de no máximo 2 frases sobre o risco e a tendência atual. 
    Responda em Português.
    """
    try:
        response = ollama.chat(model='llama3.2', messages=[
            {'role': 'user', 'content': prompt},
        ])
        return response['message']['content']
    except Exception as e:
        return f"Erro ao conectar com Ollama: {e}"

def main():
    print("🚀 Iniciando coleta de dados...")
    
    # 2. COLETA DE DADOS
    gold = yf.Ticker("GC=F")
    data = gold.history(period="5d")
    
    if data.empty:
        logging.error("Falha ao baixar dados do Yahoo Finance")
        return

    # 3. CÁLCULOS (ENGINEERING)
    average_price = data['Close'].mean()
    std_dev = data['Close'].std()
    last_price = data['Close'].iloc[-1]
    prev_price = data['Close'].iloc[-2]
    change_pct = ((last_price - prev_price) / prev_price) * 100

    # 4. CHAMADA DA IA
    print("🧠 Solicitando análise para a IA local (Llama 3.2)...")
    analise_texto = pedir_analise_ia(average_price, std_dev, change_pct)

    # 5. EXIBIÇÃO E LOGGING
    output = f"""
    --- RELATÓRIO DE MERCADO ---
    Média: ${average_price:.2f}
    Variação: {change_pct:+.2f}%
    Análise da IA: {analise_texto}
    ----------------------------
    """
    print(output)
    logging.info(f"Dados processados. Variação: {change_pct:.2f}%. Análise IA: {analise_texto}")

if __name__ == "__main__":
    main()
  

