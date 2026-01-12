import yfinance as yf
import logging
from datetime import datetime

# Configura o LOG para salvar em um arquivo chamado 'gate_history.log'
logging.basicConfig(
    filename='gate_history.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def quality_gate_validator(ticker, asset_name):
    print(f"--- Starting Validation: {asset_name} ({ticker}) ---")
    
    # Baixa os dados
    data = yf.download(ticker, period="5d", interval="1d")
    
    if data.empty:
        msg = f"ERROR: No data found for {asset_name}."
        print(f"❌ {msg}")
        logging.error(msg)
        return
    
    # 1. VALIDAÇÃO (O "Portão" de Segurança)
    if data.isnull().values.any():
        msg = f"REJECTED: Null values in {asset_name} data."
        print(f"❌ {msg}")
        logging.warning(msg)
        return # Para aqui se o dado estiver sujo
    else:
        print(f"✅ DATA QUALITY: {asset_name} data is clean.")

    # 2. FEATURE ENGINEERING (A Inteligência)
    # Calculamos a média do preço de fechamento ('Close') dos últimos 5 dias
    # 2. FEATURE ENGINEERING (A Inteligência)
    # Adicionamos .item() para converter o resultado do Pandas em um número comum
    average_price = data['Close'].mean().item()
    
    msg_media = f"5-Day Average {asset_name} Price: ${average_price:.2f}"
    print(f"📊 INFO: {msg_media}")
    logging.info(msg_media)

def new_func(asset_name, data):
    average_price = data['Close'].mean()
    
    msg_media = f"INFO: 5-Day Average {asset_name} Price: ${average_price:.2f}"
    return msg_media# Salva a média no histórico de Logs

if __name__ == "__main__":
    # Foco no Ouro
    quality_gate_validator("GC=F", "Gold Futures")
  

