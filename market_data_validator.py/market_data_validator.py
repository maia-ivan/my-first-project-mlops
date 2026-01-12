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
    
    data = yf.download(ticker, period="5d", interval="1d")
    
    if data.empty:
        msg = f"ERROR: No data found for {asset_name}."
        print(f"❌ {msg}")
        logging.error(msg)
        return
    
    # Validação de dados nulos
    if data.isnull().values.any():
        msg = f"REJECTED: Null values in {asset_name} data."
        print(f"❌ {msg}")
        logging.warning(msg)
    else:
        msg = f"PASSED: {asset_name} data is clean."
        print(f"✅ {msg}")
        logging.info(msg)

if __name__ == "__main__":
    # Foco total no Ouro
    quality_gate_validator("GC=F", "Gold Futures")
  

