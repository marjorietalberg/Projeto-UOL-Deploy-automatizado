<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0000FF&height=120&section=header" alt="Onda azul" />
</p>

<h2 align="center" style="color: #0000FF;">
  Deploy automatizado de API com FastAPI, Jenkins e Kubernetes <p>
    <p align="center">
  <img src="https://skillicons.dev/icons?i=fastapi,docker,jenkins,kubernetes" alt="Tecnologias" />
</p>
</h2>

<h1 align="center" >
  Tecnologias e Ferramentas <p>

<p align="center">  
  <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white"/>
  <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white"/>
  <img src="https://img.shields.io/badge/Jenkins-d24939?style=for-the-badge&logo=jenkins&logoColor=white"/>
  <img src="https://img.shields.io/badge/Kubernetes-326ce5?style=for-the-badge&logo=kubernetes&logoColor=white"/>
  <img src="https://img.shields.io/badge/React-20232a?style=for-the-badge&logo=react&logoColor=61dafb"/>
  <img src="https://img.shields.io/badge/Node.js-339933?style=for-the-badge&logo=node.js&logoColor=white"/>
</p></h1>

| Tecnologia     | Descrição |
|----------------|-----------|
| 🐍 **FastAPI** | Framework web em Python para criar APIs rápidas e eficientes |
| 🐳 **Docker** | Containerização da aplicação para ambientes portáteis |
| 📦 **Docker Hub** | Registro remoto para distribuição das imagens |
| 🧰 **Jenkins** | Ferramenta de integração e entrega contínua (CI/CD) |
| ☸️ **Kubernetes** | Orquestração de contêineres com escalabilidade |
| 🟢 **Node.js** | Backend assíncrono e leve usado em parte do serviço |
| ⚛️ **React** | Frontend moderno e reativo para consumo da API |

---

## Sumário 📝

- [Descrição Geral](README.md#descricao-geral)  
- [Tecnologias Utilizadas](README.md#tecnologias-utilizadas)  
- [Fases do Projeto](README.md#fases-do-projeto)  
- [Executando Localmente](README.md#executando-localmente)  

---

- [Fase 1 - Preparação do Projeto](./Fases/01-Preparacao-do-Projeto/README.md)  
- [Fase 2 - Conteinerização com Docker](./Fases/02-Conteinerizacao-com-Docker/README.md)  
- [Fase 3 - Deploy no Kubernetes](./Fases/03-Arquivos-de-Deploy-no-Kubernetes/README.md)  
- [Fase 4 - Jenkins: Build e Push](./Fases/04-Jenkins-Build-Push/README.md)  
- [Fase 5 - Jenkins: Deploy no Kubernetes](./Fases/05-Jenkins-Deploy-no-Kubernetes/README.md)  
- [Fase 6 - Documentação](./Fases/06-Documentacao/README.md)  
- [Desafios Extras](./Fases/07-Desafios-Extras/README.md)
  
---

### [Fase 1 - Preparação do Projeto](./Fases/01-Preparacao-do-Projeto/README.md)

Nesta fase inicial, o foco é estabelecer toda a infraestrutura básica necessária para o desenvolvimento do projeto. Isso inclui:

- Criar o repositório no GitHub para versionamento do código;
- Criar conta no Docker Hub para armazenar as imagens Docker;
- Verificar o acesso e configuração do cluster Kubernetes local;
- Validar que a aplicação FastAPI roda localmente usando o servidor Uvicorn.

---

### [Fase 2 - Conteinerização com Docker](./Fases/02-Conteinerizacao-com-Docker/README.md)

Objetivo de empacotar a aplicação em containers Docker para facilitar o deploy e a escalabilidade:

- Criar Dockerfile para frontend e backend;
- Opcionalmente, criar docker-compose para testes locais;
- Executar build da imagem Docker e enviar para Docker Hub;
- Versionar os Dockerfiles no repositório GitHub.

---

### [Fase 3 - Deploy no Kubernetes](./Fases/03-Arquivos-de-Deploy-no-Kubernetes/README.md)

Esta fase visa implantar a aplicação conteinerizada no cluster Kubernetes local:

- Criar os manifests YAML para deployment e service da aplicação;
- Aplicar os manifests no cluster;
- Testar e garantir que a aplicação esteja acessível via Kubernetes.

---

### [Fase 4 - Jenkins: Build e Push](./Fases/04-Jenkins-Build-Push/README.md)

Automatizar a construção e distribuição das imagens Docker usando Jenkins:

- Criar pipeline no Jenkins para build e push da imagem;
- Configurar webhook no GitHub para disparar a pipeline automaticamente;
- Garantir que a pipeline execute o build e push sem intervenção manual.

---

### [Fase 5 - Jenkins: Deploy no Kubernetes](./Fases/05-Jenkins-Deploy-no-Kubernetes/README.md)

Automatizar o deploy da aplicação no Kubernetes via Jenkins:

- Configurar Jenkins para usar `kubectl` com o kubeconfig do cluster;
- Adicionar etapa de deploy no Jenkinsfile que aplica os manifests no Kubernetes;
- Testar pipeline completa: build, push e deploy automatizados.

---

### [Fase 6 - Documentação](./Fases/06-Documentacao/README.md)

Documentar todo o processo para garantir reprodução e manutenção do projeto:

- Criar README.md detalhado com passo a passo;
- Incluir prints do Jenkins e resultados dos testes;
- Apresentar o fluxo completo da pipeline funcionando.

---

- [Desafios Extras](https://github.comProject3-CompassUOL-DevSecOps/tree/main/Fases/07-Desafios-Extras)  
  -  Após o push da imagem do container, criar uma etapa para realizar o scanner de vulnerabilidades utilizando o **Trivy**.  
  -  Configurar um webhook no **Slack** ou **Discord** para notificar sempre que a pipeline atualizar o ambiente Kubernetes.  
  -  Implantar o **SonarQube** em ambiente Docker, integrá-lo com o Jenkins e enviar todo o código da aplicação para análise estática (SAST).  
  -  Utilizar **Helm Chart** para fazer a implantação da aplicação no Kubernetes.  




<p align="center">    
  <img src="https://github.com/user-attachments/assets/79a2e995-a1be-4192-9ded-771004ef7417" width="250">
</p>
