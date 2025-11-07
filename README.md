# Projeto CI/CD  
<<<<<<< HEAD
![badge](https://img.shields.io/badge/Git-%23F05032?style=for-the-badge&logo=git&logoColor=white&logoSize=auto)  
![GITHUBACTIONS](https://img.shields.io/badge/githubactions-%232088FF?style=for-the-badge&logo=githubactions&logoColor=white&logoSize=auto)  
![RANCHER](https://img.shields.io/badge/rancher-%230075A8?style=for-the-badge&logo=rancher&logoColor=white)  
![ARGOCD](https://img.shields.io/badge/argocd-%23EF7B4D?style=for-the-badge&logo=argo&logoColor=white)  
=======
![badge](https://img.shields.io/badge/Git-%23F05032?style=for-the-badge&logo=git&logoColor=white&logoSize=auto)
![GITHUBACTIONS](https://img.shields.io/badge/githubactions-%232088FF?style=for-the-badge&logo=githubactions&logoColor=white&logoSize=auto)
![RANCHER](https://img.shields.io/badge/rancher-%230075A8?style=for-the-badge&logo=rancher&logoColor=white)
![ARGOCD](https://img.shields.io/badge/argocd-%23EF7B4D?style=for-the-badge&logo=argo&logoColor=white)
>>>>>>> 81fd3511e0c6dabc901be096b4324dfd5904eec5
![KUBERNETES](https://img.shields.io/badge/kubernetes-%23326CE5?style=for-the-badge&logo=kubernetes&logoColor=white)

Esse projeto tem o objetivo de automatizar um ciclo completo de desenvolvimento. Utilizando uma aplicação **FastAPI** simples, **GitHub Actions**, **DockerHub** e **ArgoCD**, teremos um ciclo de entrega contínua (CI/CD).

---

### 🧩 Requisitos:
- Conta no GitHub  
- Conta no DockerHub  
- Rancher Desktop com Kubernetes  
- Kubectl configurado  
- ArgoCD no cluster local  
- Git instalado  
- Python 3  

---

### 🚀 Criando a Aplicação FastAPI

Crie **2 repositórios públicos** no GitHub:  

#### 🗂 Repositório 1: `Projeto-GitActions`
Em uma pasta no seu PC, clone este repositório e dê um *push* no **seu** repositório:

```bash
cd C:\anale\projetoGitActions
git clone https://github.com/ana-bia07/Projeto-GitActions.git
git remote add origin http://<Seu-repositorio-main-python>
git add .
git commit -m "Clonando repositório"
git push origin main
```

#### 🗂 Repositório 2: `hello-manifests`
Em outra pasta, clone o repositório:  
https://github.com/ana-bia07/hello-manifests

```bash
cd C:\anale\manifests
git clone https://github.com/ana-bia07/hello-manifests
git remote add origin http://<Seu-repositorio-hello-manifests>
git add .
git commit -m "Clonando repositório"
git push origin main
```

Crie também um repositório público no **DockerHub**:  
#### `nome-de-usuario/main-python`
Deixe-o vazio.

---

### 🧾 Explicando os Arquivos:
- **main.py:** contém a aplicação FastAPI.  
- **requirements.txt:** lista todas as dependências necessárias para a aplicação (o `[standard]` indica o tipo desejado).  
- **Dockerfile:** arquivo necessário para criar a imagem Docker do `main.py`.  
- **post.yaml:** responsável por configurar o *workflow* e automatizar parte do processo de deploy.

---

### 🔐 Configuração de Secrets

Você deve ter reparado que o arquivo `post.yaml` utiliza variáveis como  
`DOCKER_USERNAME: ${{ secrets.DOCKER_USERNAME }}` para login no Docker e configuração da chave SSH.  
Vamos aprender como fazer isso:

1. **Anote seu nome de usuário e senha do DockerHub.**  
   ![docker](imagens/dockerhub.png)

2. **Acesse ou crie suas chaves SSH no GitHub.**

No PowerShell:  
Caso ainda não tenha uma chave, crie-a com:
```bash
ssh-keygen -t ed25519 -C "seu_email@exemplo.com" # cria chave
```

Ver chave pública:  
```bash
cat .\id_ed25519.pub
```

A saída será algo como:  
`ssh-ed25519 <Letras-e-números> seuemail@gmail.com`

Ver chave privada:
```bash
cat .\id_ed25519
```

A saída será parecida com:
```bash
-----BEGIN OPENSSH PRIVATE KEY-----
letras e números
-----END OPENSSH PRIVATE KEY-----
```

Agora, no GitHub, acesse:  
**Settings > SSH and GPG keys > New SSH key**  
Dê um nome e cole a **chave pública**.

![github](imagens/perfil.png)  
![github](imagens/add-key-pub.png)

---

No repositório **Projeto-GitActions**, adicione as *secrets*:  
**Settings > Secrets and variables > Actions > New repository secret**

Adicione uma para:
- `DOCKER_USERNAME`
- `DOCKER_PASSWORD`
- `SSH_PRIVATE_KEY`

![secrets](imagens/secrets.png)

Perfeito! Nosso GitHub Actions já tem todos os dados para executar as ações.


Imagem do DockerHub e atualizações:
![imagem](imagens/dockerhub-images.png)

Imagem do Repositorio hello-manifests atualizado com ultima imagem lançada:
![git](imagens/manifest.png)

---

### 🚢 ArgoCD

Agora vamos configurar o ArgoCD, que utilizará o repositório `hello-manifests` para o *deploy*.

No PowerShell, crie o namespace (lembre-se de manter o Rancher aberto em segundo plano):

```bash
kubectl create namespace argocd
```

Instale o ArgoCD:
```bash
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
```

Verifique a instalação:
```bash
kubectl get svc -n argocd
```

Crie um túnel temporário com:
```bash
kubectl port-forward svc/argocd-server -n argocd 8080:443
```

Em outro terminal (mantenha o anterior aberto), pegue a senha para login:

```bash
[System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String($(kubectl get secret argocd-initial-admin-secret -n argocd -o jsonpath="{.data.password}")))
```

Acesse: [http://localhost:8080](http://localhost:8080)  
Usuário: `admin`  
Senha: cole a senha exibida no terminal  

![argo](imagens/argologin.png)

Crie uma aplicação com seu repositório `hello-manifests`:  
![argo](imagens/config-parte1.png)  
![argo](imagens/config-parte2.png)  
![argo](imagens/finish.png)

Aguarde até **10 minutos**, pois pode demorar.  
Depois, execute novamente:
```bash
kubectl get svc
```

![powershell2](imagens/getsvc.png)

Interrompa o terminal anterior (`Ctrl + C`) e execute:
```bash
kubectl port-forward svc/app-fastapi 8080:8080
```

Acesse [http://localhost:8080](http://localhost:8080)  
![imagem](imagens/primeira.png)  

Acessando http://localhost:8080/saudacao/{nome}
![imagens](imagens/concluido.png)

---

## 🎉 Parabéns!
Você conseguiu automatizar o processo de desenvolvimento!  
Caso tenha dúvidas, os arquivos estão documentados linha por linha, explicando a função de cada trecho.  

📚 Recomendo consultar:  
- [Comandos Docker](https://docs.docker.com/build/ci/github-actions/)  
- [Comandos Git](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax)
