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


