## Projeto CI/CD
---
Esse projeto tem o objetivo de automatizar um ciclo completo de desinvolvimento. Utilizando uma aplicação FastAPI simples, GitActions, DockerHub e ArgoCD teremos um ciclo de entrega contínua. 
---
### Requisitos:
- Conta no GitHub
- Conta no DockerHub
- Rancher Desktop com Kubernets
- Kubectl configurado
- ArgoCd no cluster local
- Git instalado
- Python 3 
---
### Criando Aplicação FastAPI

Crie 2 repositorios publicos no github: 
#### Projeto-GitActions
- Em uma pasta no seu PC, clone esse repositorio e de um push no **seu** repositorio:
```bash
cd C:\anale\projetoGitActions
git clone https://github.com/ana-bia07/Projeto-GitActions.git
git remote add origin http://<Seu repositorio main-python>
git add .
git commit -m "Clonando repositorio"
git push origin main
```
#### hello-manifests
- Em outra pasta, clone o repositorio: https://github.com/ana-bia07/hello-manifests
```bash
cd C:\anale\manifests
git clone https://github.com/ana-bia07/hello-manifests
git remote add origin http://<Seu repositorio hello-manifests>
git add .
git commit -m "Clonando repositorio"
git push origin main
```
Criar um repositorio publico no DockeHub:
#### <nome-de-usuario>/main-python:
- vazio

**Explicando arquivos:**
- **main.py:** la esta a nossa aplicação que utiliza o fastAPI para facilitar
-**requeriments.txt:** la esta toda as dependencias necessarias para a nossa aplicação, o [standard] deixa claro o tipo que queremos
-**Dockerfile:** é o arquivo necessario para criar uma imagem do nosso arquivo main.py
-**post.yaml:** é o responsavel por configurar o nosso workflow e parte da automatização da nossa aplicação
---
### Configurações de Secrets
Você deve ter reparado que o nosso arquivo post.yaml utiliza variaveis como `DOCKER_USERNAME: ${{secrets.DOCKER_USERNAME}}` para fazer login docker ou configuração de chave ssh. Vamos aprender como faz.
- Primeiro deve anotas seu nick do DockerHub e senha.
![docker](imagens/dockerhub.png)

- Segundo vamos acessar nossas chaves ssh do github.
No PowerShell:
Caso ainda não tenha, crie uma com:
```bash
ssh-keygen -t ed25519 -C "seu_email@exemplo.com" #cria chave
```
Ver chave publica: 
```bash
cat .\id_ed25519.pub
```
A saida deve ser parecida com isso: `ssh-ed25519 <Letras-e-numeros> seuemail@gmail.com`
Ver chave privada:
```bash
cat .\id_ed25519
```
a saida deve ser parecida com isso:
```bash
-----BEGIN OPENSSH PRIVATE KEY-----
letras e numeros
-----END OPENSSH PRIVATE KEY-----
```
- Agora no github, acesse no seu perfil: **Settings** > **SSH and GPG keys** > **New SSH key**
  Coloque o nome que desejar e cole a chave publica.

![github](imagens/perfil.png)
![github](imagens/add-key-pub.png)

- No repositorio **Projeto-GitActions** vamos adicionar as secrets: Acesse o repositorio > **Settings** > **Secrets and variables** > **Actions** > **New repository secrets** E adicione uma para o nome do dockerhub, outro para a senha e um para a ssh privada.
![secrets](imagens/secrets.png)

Perfeito! Nosso GitActions tem todos os dados para executar as açôes.

### ArgoCD




. cria o deploy e add no reopsitorio semarado chamado hello-manifests

1. mesmo esquema do outro argo.
2. cria namespace
3. baixa argo
4. baixa cli
5. pega a senha
6. abre o tunel
7. entra em localhost:8080 e login
