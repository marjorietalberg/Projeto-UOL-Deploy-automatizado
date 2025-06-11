<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0000FF&height=120&section=header" alt="Onda azul" />
</p>

# Deploy da Aplicação no Kubernetes

### Objetivo
- [x] Criar e aplicar os arquivos YAML de Deployment e Service para rodar a aplicação no Kubernetes local
- [x] Expor a aplicação para acesso externo via NodePort na porta 30001 ou usando port-forward.
- [x] arantir que a aplicação esteja rodando e acessível via Kubernetes.

### Passo 1: Criar o arquivo deployment.yaml
Este arquivo define o Deployment que irá criar o Pod com sua aplicação FastAPI.
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
          imagePullPolicy: Never
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

### Passo 2: Criar o arquivo service.yaml
Este arquivo cria um Service do tipo NodePort para expor a aplicação na porta 30001.
```bash
apiVersion: v1
kind: Service
metadata:
  name: fastapi-service
spec:
  selector:
    app: fastapi-backend
  type: NodePort
  ports:
    - protocol: TCP
      port: 80
      targetPort: 8000
      nodePort: 30001

```
