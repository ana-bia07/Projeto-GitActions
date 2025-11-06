# Projeto CI/CD
![bagde](https://img.shields.io/badge/Git-%23F05032?style=for-the-badge&logo=git&logoColor=white&logoSize=auto)
![GITHUBACTIONS](https://img.shields.io/badge/githubactions-%232088FF?style=for-the-badge&logo=githubactions&logoColor=white&logoSize=auto
)
![RANCHER](https://img.shields.io/badge/ranher-%230075A8?style=for-the-badge&logo=rancher&logoColor=white)
![ARGOCD](https://img.shields.io/badge/argocd-%23EF7B4D?style=for-the-badge&logo=argo&logoColor=white)
![KUBERNETES](https://img.shields.io/badge/kubernetes-%23326CE5?style=for-the-badge&logo=kubernetes&logoColor=white)

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
#### Repositorio 1: Projeto-GitActions
- Em uma pasta no seu PC, clone esse repositorio e de um push no **seu** repositorio:
```bash
cd C:\anale\projetoGitActions
git clone https://github.com/ana-bia07/Projeto-GitActions.git
git remote add origin http://<Seu repositorio main-python>
git add .
git commit -m "Clonando repositorio"
git push origin main
```
#### Repositorio 2: hello-manifests
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
#### nome de usuario/main-python:
* vazio

**Explicando arquivos:**
- **main.py:** la esta a nossa aplicação que utiliza o fastAPI para facilitar
- **requeriments.txt:** la esta toda as dependencias necessarias para a nossa aplicação, o [standard] deixa claro o tipo que queremos
- **Dockerfile:** é o arquivo necessario para criar uma imagem do nosso arquivo main.py
- **post.yaml:** é o responsavel por configurar o nosso workflow e parte da automatização da nossa aplicação
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
---
![github](imagens/add-key-pub.png)

- No repositorio **Projeto-GitActions** vamos adicionar as secrets: Acesse o repositorio > **Settings** > **Secrets and variables** > **Actions** > **New repository secrets** E adicione uma para o nome do dockerhub, outro para a senha e um para a ssh privada.
![secrets](imagens/secrets.png)

Perfeito! Nosso GitActions tem todos os dados para executar as açôes.

### ArgoCD
Agora vamos configurar nosso argocd que vai utilizar o arquivo do manifests para deploy.
No PowerShell vamos criar uma namespace: (lembre de estar como rancher aberto segundo plano)
```bash
kubectl create namespace argocd
```
Agora instalamos o argocd:
```bash
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
```
Verifique a instalação:
```bash
kubectl get svc -n argocd
```
Agora usamos o `port-forward` para criar um tunel temporario:
```bash
kubectl port-forward svc/argocd-server -n argocd 8080:443
```
Em outro terminal (deixe esse primeiro aberto), vamos pegar a senha para fazer o login no argo:
```bash
[System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String($(kubectl get secret argocd-initial-admin-secret -n argocd -o jsonpath="{.data.password}")))
```
Acesse: [localhost://8080](http://localhost:8080)
Usuario: admin
Senha: Cole a senha exibida no terminal
![argo](imagens/argologin.pgn)

- Vamos criar uma aplicação com nosso repositorio hello-manifests:
![argo](imagens/config-parte1.png)
![argo](imagens/config-parte2.png)
![argo](imagens/finish.png)

Aguarde por ate 10 minutos pois pode demorar. Execute novamente o comando:
```bash
kubectl get svc
```
![powershell2](imagens/getsvc.png)

De um ctrl + c na powershell antiga e execute:
```bash
kubectl port-forward svc/app-fastapi 8080:8080
```
Acesse [localhost://8080](http://localhost:8080)

![imagens](imagens.concluido.png)

---

## Parabéns
Você conseguiu automatizar o processo de desenvolvimento, caso tenha alguma duvida, os arquivos estão documentados por linha com a função que cada uma faz. Recomendo usar documentação facil quando usar gitActions:
[Comandos docker](https://docs.docker.com/build/ci/github-actions/)

[Comandos Git](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax)