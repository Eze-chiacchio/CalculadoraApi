FROM python:3.9
WORKDIR /calculadoraapi
COPY requeriments.txt calculadoraapi/requeriments.txt
RUN pip install --no-cache-dir --upgrade -r /calculadoraapi/requeriments.txt
COPY . .
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
