from fastapi.testclient import TestClient

from src.main import app
from src.config import settings

client = TestClient(app)


headers = {"Authorization": f"Bearer {settings.API_KEY}"}


def test_health_endpoint():
    response = client.get("/health", headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert "version" in data


def test_generate_molecule_endpoint():
    payload = {"base_smiles": "CC(=O)OC1=CC=CC=C1C(=O)O", "num_mutations": 1}
    response = client.post("/generate_molecule", json=payload, headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert "generated_smiles" in data
    assert "molecular_image" in data
    assert "properties" in data


def test_generate_molecule_validation():
    # Test empty base_smiles
    payload = {"base_smiles": "", "num_mutations": 1}
    response = client.post("/generate_molecule", json=payload, headers=headers)
    assert response.status_code == 400

    # Test negative num_mutations
    payload = {"base_smiles": "CCO", "num_mutations": -1}
    response = client.post("/generate_molecule", json=payload, headers=headers)
    assert response.status_code == 400
