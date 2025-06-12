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

        stage('Verificar arquivos Kubernetes') {
            steps {
                script {
                    sh '''
                        echo "📁 Listando arquivos na raiz do projeto:"
                        ls -l
                        echo ""
                        echo "📄 Conteúdo de deployment.yaml:"
                        cat deployment.yaml || echo "Arquivo deployment.yaml não encontrado!"
                        echo ""
                        echo "📄 Conteúdo de service.yaml:"
                        cat service.yaml || echo "Arquivo service.yaml não encontrado!"
                    '''
                }
            }
        }

        stage('Deploy no Kubernetes') {
            steps {
                withCredentials([file(credentialsId: 'kubeconfig', variable: 'KUBECONFIG_FILE')]) {
                    script {
                        sh '''
                            # Copia o arquivo kubeconfig para o workspace para garantir leitura correta
                            cp "$KUBECONFIG_FILE" ./kubeconfig
                            export KUBECONFIG=$PWD/kubeconfig

                            echo "🌐 Contexto atual do Kubernetes:"
                            kubectl config current-context || exit 1

                            echo "🚀 Aplicando deployment.yaml..."
                            kubectl apply -f deployment.yaml || exit 1

                            echo "🚀 Aplicando service.yaml..."
                            kubectl apply -f service.yaml || exit 1
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
            echo '❌ Erro no pipeline. Verifique os logs acima.'
        }
    }
}
