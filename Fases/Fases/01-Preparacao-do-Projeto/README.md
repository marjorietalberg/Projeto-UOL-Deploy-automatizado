<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0000FF&height=120&section=header" alt="Onda azul" />
</p>



# FASE 1: Preparação do Projeto
## Objetivos:
- [x] Repositório GitHub com branch dev

- [x] Conta no Docker Hub

- [x] Teste local com FastAPI (usando uvicorn)

- [x] Acesso a um cluster Kubernetes local (ex: minikube ou kind)

### 📌 1. Criar repositório no GitHub
> Exemplo :

```bash
git init
git remote add origin https://github.com/seu-usuario/nome-repo.git
git add .
git commit -m "first commit"
git push -u origin master
```
> Crie a branch dev:

```bash
git checkout -b dev
git push -u origin dev
```


### 📌 2. Criar conta no Docker Hub

👉 Acesse: https://hub.docker.com/

### 📌 3. Verificar Kubernetes local
 > Para minikube:

```bash
minikube start
kubectl get nodes
```
 > Para kind:
```bash
kind create cluster
kubectl cluster-info
```

### 📌 4. Validar execução com uvicorn
> Se for FastAPI:
```bash
uvicorn main:app --reload
```

## 📤 Entregáveis:
> Código funcionando localmente

> GitHub com branch master e dev

> Kubernetes local configurado

