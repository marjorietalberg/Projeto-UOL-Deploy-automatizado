<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0000FF&height=120&section=header" alt="Onda azul" />
</p>

<p align="center">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/docker/docker-original.svg" alt="Docker Icon" width="200" style="margin-right: 20px;" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/linux/linux-original.svg" alt="Linux Icon" width="200" />
</p>


# FASE 2: Docker e Docker Hub
### Objetivo:
- [x] Criar Dockerfile

- [x] Executar com Docker Compose (opcional)

- [x] Enviar para o Docker Hub
    
### 1. Criar o arquivo deployment.yaml
Este arquivo define o Deployment e o Service do Kubernetes para o seu backend FastAPI.

```bash
apiVersion: apps/v1
kind: Deployment
metadata:
  name: fastapi-backend
spec:
  replicas: 1
  selector:
    matchLabels:
      app: fastapi-backend
  template:
    metadata:
      labels:
        app: fastapi-backend
    spec:
      containers:
        - name: fastapi-backend
          image: marjorie02/fastapi-backend:latest
          ports:
            - containerPort: 8000
---
apiVersion: v1
kind: Service
metadata:
  name: fastapi-service
spec:
  selector:
    app: fastapi-backend
  ports:
    - protocol: TCP
      port: 80
      targetPort: 8000
  type: NodePort

```
 > Deployment: Cria 1 réplica do container usando a imagem Docker do backend FastAPI.

> Service: Expõe a aplicação na porta 80 do cluster, redirecionando para a porta 8000 do container.

> NodePort: Permite acesso externo ao cluster em uma porta dinâmica (geralmente entre 30000 e 32767).

### 2. Aplicar o arquivo no Kubernetes
> Dentro da pasta onde está o arquivo deployment.yaml, execute:
```bash
kubectl apply -f deployment.yaml

```
> Isso criará (ou atualizará) o Deployment e o Service.

### 3. Verificar os pods e serviços
Para verificar se o pod do backend está rodando:
```bash
kubectl get pods

```
> Para verificar os serviços e descobrir qual porta NodePort foi atribuída:
```bash
kubectl get svc

```
> Procure pela linha do serviço fastapi-service e veja a porta externa (NodePort) atribuída, por exemplo, 30080.

### 4. Acessar a API
> Você pode acessar sua API FastAPI via IP do Minikube (ou do seu cluster) e porta NodePort.

> Para pegar o IP do minikube:
```bash
minikube ip

```
### 5. Testar DNS e resolução (opcional)
Para garantir que o cluster consegue puxar imagens, crie um pod temporário com a imagem busybox:
```bash
kubectl run -i --tty dnsutils --image=busybox --restart=Never -- sh

```

> Dentro do pod, use nslookup para testar DNS:
```bash
nslookup registry-1.docker.io
```
> Código e comandos usados
```bash
kubectl apply -f deployment.yaml
kubectl get pods
kubectl get svc
kubectl run -i --tty dnsutils --image=busybox --restart=Never -- sh
nslookup registry-1.docker.io
kubectl logs <pod-name>

```

### Nesta fase, configuramos e deployamos a API backend desenvolvida em FastAPI no cluster Kubernetes local (Minikube).

> Criamos um arquivo deployment.yaml que define:

> Um Deployment que roda a aplicação usando a imagem Docker marjorie02/fastapi-backend:latest, expondo a porta 8000.

> Um Service do tipo NodePort para expor a aplicação na rede local, redirecionando a porta 80 para a porta 8000 do container.

> Após aplicar a configuração com kubectl apply, verificamos se o pod está rodando corretamente com kubectl get pods e descobrimos a porta externa atribuída ao serviço com kubectl get svc.

> Usamos o IP do Minikube e a porta NodePort para acessar a API e visualizar a documentação automática gerada pela FastAPI (Swagger UI).

> Também testamos a resolução DNS dentro do cluster com um pod temporário baseado em busybox, garantindo que as imagens possam ser baixadas do Docker Hub sem problemas.

<p align="center">    
  <img src="https://github.com/user-attachments/assets/79a2e995-a1be-4192-9ded-771004ef7417" width="250">
</p>

