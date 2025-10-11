import pytest
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

def test_generate_molecule_endpoint():
    payload = {
        "base_smiles": "CC(=O)OC1=CC=CC=C1C(=O)O",
        "num_mutations": 1
    }
    response = client.post("/generate_molecule", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "generated_smiles" in data
    assert "molecular_image" in data
    assert "properties" in data