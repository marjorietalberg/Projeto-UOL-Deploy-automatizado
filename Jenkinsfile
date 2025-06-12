pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "marjorie02/fastapi-backend:latest"
    }

    stages {
        stage('Clonar Repositório') {
            steps {
                echo '🔄 Clonando repositório...'
                git branch: 'main', url: 'https://github.com/marjorietalberg/Projeto-UOL-Deploy-automatizado.git'
            }
        }

        stage('Build da Imagem Docker') {
            steps {
                echo '🐳 Construindo a imagem Docker...'
                script {
                    docker.build("${DOCKER_IMAGE}", "backend/")
                }
            }
        }

        stage('Push para Docker Hub') {
            steps {
                echo '🚀 Enviando imagem para Docker Hub...'
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
                echo '📦 Aplicando configuração no Kubernetes...'
                withCredentials([file(credentialsId: 'kubeconfig', variable: 'KUBECONFIG_FILE')]) {
                    withEnv(["KUBECONFIG=$KUBECONFIG_FILE"]) {
                        sh '''
                            kubectl apply -f backend/deployment.yaml
                            kubectl apply -f backend/service.yaml
                        '''
                    }
                }
            }
        }
    }

    post {
        success {
            echo '✅ Deploy realizado com sucesso!'
            chucknorris()  // <-- Plugin Chuck Norris executado em sucesso
        }
        failure {
            echo '❌ Erro no pipeline.'
            chucknorris()  // <-- Plugin Chuck Norris executado em falha também para animar
        }
    }
}
