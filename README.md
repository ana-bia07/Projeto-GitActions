1. primeiro o arquivo main, py 
2. depois requeriments.txt (precisa do stardard para instalar outras dependencias como o uvicorn q vamos usar)
3. avitar o ambiente: primeiro cria python -m venv venv e depois ativa: .\venvzScripts\Activate.ps1
4. instalar pacotes: pip install -r .\requirements.txt
5. testar execução

1. criar o dockerfile
2. testar com comando: docker build -t hello-word .
3. testar local: docker run -d -p 8081:80 --name fastapi-teste hello-word:latest
4. docker ps pra ver se ta rodando e http://localhost:8081/