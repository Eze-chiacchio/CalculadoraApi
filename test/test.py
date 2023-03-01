from fastapi import FastAPI
from fastapi.testclient import TestClient
from src.init import app 

client = TestClient(app)

def test_suma():
    response = client.get("/mul",headers={"num1":2,"num2":3})
    assert response.status_code == 200
    assert response.json() == [6]