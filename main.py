from fastapi import FastAPI

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