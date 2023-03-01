from fastapi import FastAPI
from fastapi.testclient import TestClient

app = FastAPI()

@app.get("/plus")
def suma(num1,num2):
    resultado = int(num1) + int(num2)
    return{resultado}

@app.get("/minus")
def resta(num1,num2):
    resultado = int(num1) - int(num2)
    return{resultado}

@app.get("/div")
def div(num1,num2):
    if num2 != "0":
        resultado = int(num1) / int(num2)
        return{resultado}
    else:
        return{"No se puede dividir por 0"}

@app.get("/mul")
def multiplicacion(num1,num2):
    resultado = int(num1) * int(num2)
    return{resultado}

client = TestClient(app)

def test_suma():
    response = client.get("/mul",headers={"num1":2,"num2":3})
    assert response.status_code == 200
    assert response.json() == [6]
