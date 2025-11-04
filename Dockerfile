#imagem base
FROM python:3.10-slim 
#diretorio de trabalho, se não existir ele cria
WORKDIR /app
#copia o arquivo para a pasta do workdir
COPY requirements.txt .
# executa o comando
RUN pip install --no-cache-dir -r requirements.txt

COPY main.py .
#porta usada dentro do container
EXPOSE 80
#comando principal que é executado quando o container iniciar
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]