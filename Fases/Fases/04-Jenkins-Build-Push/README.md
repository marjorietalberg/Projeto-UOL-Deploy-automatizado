<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0000FF&height=120&section=header" alt="Onda azul" />
</p>

<p align="center">
  <img src="https://www.jenkins.io/images/logos/jenkins/jenkins.svg" alt="Jenkins Icon" width="130" style="vertical-align: middle;" />
  &nbsp;&nbsp;&nbsp;&nbsp;
  <img src="https://www.vectorlogo.zone/logos/docker/docker-icon.svg" alt="Docker Icon" width="170" style="vertical-align: middle;" />
</p>


# Jenkins - Build e Push da Imagem Docker

### Objetivo
- [x] az o build da imagem Docker do backend FastAPI.
- [x] Faz o push para o Docker Hub.
- [x] É acionada automaticamente ao fazer git push no GitHub

 ### Preparar o Jenkins
- [x] enha o Jenkins instalado e rodando.
- [x] nstale o plugin Docker Pipeline para poder usar comandos Docker dentro do Jenkinsfile.
- [x] Configure as credenciais do Docker Hub no Jenkins (com seu usuário e token/senha) em Manage Jenkins > Credentials.


### Passo 2: Criar Jenkinsfile básico para build e push
```bash
pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "marjorie02/fastapi-backend:latest"
    }

    stages {
        stage('Clonar Repositório') {
            steps {
                git branch: 'main', url: 'https://github.com/marjorietalberg/Projeto-UOL-Deploy-automatizado.git'
            }
        }

        stage('Build da Imagem Docker') {
            steps {
                script {
                    docker.build("${DOCKER_IMAGE}")
                }
            }
        }

        stage('Push para Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    script {
                        sh "echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin"
                        sh "docker push ${DOCKER_IMAGE}"
                    }
                }
            }
        }

        stage('Deploy no Kubernetes') {
            steps {
                withCredentials([file(credentialsId: 'kubeconfig', variable: 'KUBECONFIG_FILE')]) {
                    withEnv(["KUBECONFIG=$KUBECONFIG_FILE"]) {
                        dir('backend') {
                            sh '''
                                kubectl apply -f deployment.yaml
                                kubectl apply -f service.yaml
                            '''
                        }
                    }
                }
            }
        }
    }

    post {
        success {
            echo '✅ Deploy realizado com sucesso!'
        }
        failure {
            echo '❌ Erro no pipeline.'
        }
    }
}

```
###  2. Adicionar credenciais no Jenkins
> Vá até Jenkins > Manage Jenkins > Credentials > (Global)

> Clique em Add Credentials:

> Tipo: Username with password

> ID: dockerhub

> Username: marjorie02 (seu usuário Docker Hub)

> Password: (sua senha do Docker Hub)

 ### 3. Criar Pipeline no Jenkins
> Vá em http://localhost:8080 ou http://<IP_DO_SERVIDOR>:8080

> Clique em "New Item"

> Nomeie como: pipeline-uol-ci

> Selecione: Pipeline

> Vá na aba Pipeline

> Configure como:

```bash
Definition: Pipeline script from SCM
SCM: Git
Repository: https://github.com/marjorietalberg/Projeto-UOL-Deploy-automatizado.git
Branch: main
Script Path: backend/Jenkinsfile
```
