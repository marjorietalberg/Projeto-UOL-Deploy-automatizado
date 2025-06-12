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
                    docker.build("${DOCKER_IMAGE}", "backend/")
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
        
        // Stage extra para conferir arquivos antes do deploy
        stage('Verificar arquivos Kubernetes') {
            steps {
                script {
                    sh '''
                    echo "Listando arquivos na pasta backend:"
                    ls -l backend/
                    echo ""
                    echo "Conteúdo de backend/deployment.yaml:"
                    cat backend/deployment.yaml
                    echo ""
                    echo "Conteúdo de backend/service.yaml:"
                    cat backend/service.yaml
                    '''
                }
            }
        }

        stage('Deploy no Kubernetes') {
            steps {
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
        }
        failure {
            echo '❌ Erro no pipeline.'
        }
    }
}
