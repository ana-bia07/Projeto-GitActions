from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
  return {"message": "Funcionou!!! Go drinking"}

@app.get("/saudacao/{nome}", response_class=HTMLResponse)
async def saudacao(nome: str):
    html_content = f"""
    <html>
        <head>
            <title>Saudação 💫</title>
            <style>
                body {{
                    background-color: #1f2833;
                    color: #45a29e;
                    font-family: 'Segoe UI', sans-serif;
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                    justify-content: center;
                    height: 100vh;
                    margin: 0;
                }}
                h1 {{
                    font-size: 2.5em;
                    margin-bottom: 10px;
                }}
                p {{
                    font-size: 1.2em;
                    color: #c5c6c7;
                }}
            </style>
        </head>
        <body>
            <h1>👋 Olá, {nome}!</h1>
            <p>Seja bem-vindo(a) ao FastAPI estilizado 💜</p>
        </body>
    </html>
    """
    return html_content