from fastapi.testclient import TestClient
from src.main import app
import pytest

client = TestClient(app)

def test_read_home():
    """Testa se a rota principal responde 200 OK"""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["status"] == "online"

def test_analise_ouro_formato():
    """Testa se a rota de análise retorna os campos esperados"""
    # Nota: Este teste pode demorar porque chama o Ollama
    response = client.get("/analisar/ouro")
    assert response.status_code == 200
    dados = response.json()
    assert "ativo" in dados
    assert "analise_ia" in dados
    assert dados["ativo"] == "Ouro"
    