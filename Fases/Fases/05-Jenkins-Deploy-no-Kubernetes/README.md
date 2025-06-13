<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0000FF&height=120&section=header" alt="Onda azul" />
</p>

<p align="center">
  <img src="https://www.jenkins.io/images/logos/jenkins/jenkins.svg" alt="Jenkins Icon" width="150" valign="middle" />
  &nbsp;&nbsp;&nbsp;&nbsp;
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/kubernetes/kubernetes-plain.svg" alt="Kubernetes Icon" width="150" valign="middle" />
</p>

# Jenkins – Deploy no Kubernetes

### Objetivo 

- [x] Integrar o Jenkins com o `kubectl`, usando o `kubeconfig` do cluster.
- [x] Adicionar uma etapa de deploy no `Jenkinsfile`.
- [x] Criar arquivos de manifesto Kubernetes (`deployment.yaml`, `service.yaml`).
- [x] Executar o deploy automático com sucesso ao final da pipeline.



### Pré-requisitos

- Jenkins funcional (pode estar em container ou local).
- Docker e Kubernetes instalados (ex: Minikube ou Kind).
- Jenkins com plugins:
  - Docker Pipeline
  - Kubernetes CLI (opcional)
- Jenkins com `kubectl` instalado e configurado para acessar o cluster (via `~/.kube/config`).

---
###  Passo 1: Configurar Jenkins com acesso ao Kubernetes
1. Instalar kubectl no Jenkins Agent
Se Jenkins está num container, entre nele:

```bash
docker exec -it jenkins bash

```
Copiar o kubeconfig para o Jenkins
Copie o kubeconfig do cluster para Jenkins. Exemplo:
```bash
mkdir -p /var/jenkins_home/.kube
cp ~/.kube/config /var/jenkins_home/.kube/config
chmod 600 /var/jenkins_home/.kube/config
chown -R jenkins:jenkins /var/jenkins_home/.kube

```
### Passo 2: Arquivos de Deploy do Kubernetes
Crie o diretório k8s/ e os seguintes arquivos:

> k8s/deployment.yaml
>
> k8s/service.yaml

### Passo 3: Atualizar o Jenkinsfile com etapa de deploy

### Passo 4: Testar o Pipeline
Faça commit e push do Jenkinsfile, deployment.yaml e service.yaml para o repositório.

No Jenkins, clique em "Build Now".

Acompanhe as etapas:

Clone

Build da imagem

Push para Docker Hub

Deploy no cluster

Verifique se o pod está rodando:

```bash
kubectl get pods
```
### Entregáveis

| Item                        | Descrição                            |
| --------------------------- | ------------------------------------ |
| ✅ Jenkinsfile               | Pipeline com deploy automático       |
| ✅ deployment.yaml           | Deploy Kubernetes                    |
| ✅ service.yaml              | Serviço exposto                      |
| ✅ Acesso Jenkins ao cluster | `kubectl` + `kubeconfig` configurado |
| ✅ Push para Docker Hub      | Imagem publicada                     |
| ✅ Deploy automatizado       | Testado e funcionando                |
