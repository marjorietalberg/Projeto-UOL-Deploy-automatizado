<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0000FF&height=120&section=header" alt="Onda azul" />
</p>

# Desafios Extras – Jenkins CI/CD com Kubernetes

### Objetivos:
Scanner de vulnerabilidades com Trivy

Webhook para avisar via Discord (ou Slack) sobre o deploy no Kubernetes

###  1. Scanner de Vulnerabilidades com Trivy (após o push da imagem)
#### 📌 O que é o Trivy?
Trivy é uma ferramenta de scanner open-source da Aqua Security, usada para verificar vulnerabilidades em imagens Docker, repositórios de código, arquivos de configuração e pacotes do sistema.

### Instalação do Trivy no Jenkins Agent
```bash
apt update && apt install wget -y
wget https://github.com/aquasecurity/trivy/releases/latest/download/trivy_0.50.1_Linux-64bit.deb
dpkg -i trivy_0.50.1_Linux-64bit.deb

```
###  Adicionar a etapa no Jenkinsfile
Depois do push, antes do deploy

----
###  Enviar Notificação para Discord ou Slack após o Deploy
###  Objetivo:
Informar o time (via webhook) sempre que o Jenkins fizer deploy com sucesso.

### Usando Webhook do Discord
```bash
https://discord.com/api/webhooks/1352682870124187698/nFnBeaAeKRICnG0ksI25zqpGu6ZCmVMVgz3zxFPs1pACvJwB3uwuNq8AMFlselzeWDB5
```

### Etapa de Notificação no Jenkinsfile

```bash
stage('Notificar Discord') {
    when {
        expression {
            currentBuild.currentResult == 'SUCCESS'
        }
    }
    steps {
        script {
            def payload = """
            {
                "content": "✅ *Deploy realizado com sucesso no Kubernetes!* 🚀\\nImagem: `$DOCKER_IMAGE`\\nAmbiente: *produção*"
            }
            """
            writeFile file: 'discord-payload.json', text: payload
            sh 'curl -H "Content-Type: application/json" -X POST -d @discord-payload.json https://discord.com/api/webhooks/1352682870124187698/nFnBeaAeKRICnG0ksI25zqpGu6ZCmVMVgz3zxFPs1pACvJwB3uwuNq8AMFlselzeWDB5'
        }
    }
}
```
###  Entregáveis Adicionais

| Item                                     | Descrição                           |
| ---------------------------------------- | ----------------------------------- |
| ✅ Scanner Trivy                          | Verifica vulnerabilidades na imagem |
| ✅ Notificação Discord                    | Mensagem automática no canal        |
| ✅ Jenkinsfile atualizado                 | Pipeline com segurança e feedback   |
| ✅ Integração contínua + entrega contínua | Finalizada com sucesso              |


## 📌 Observação Importante – Documentação Técnica

>  Esta fase foi inteiramente documentada com foco na estrutura, comandos e práticas recomendadas para execução, mas não foi executada nem validada na prática.
>  A documentação contempla:
> 
>  Integração do Jenkins com o Kubernetes para deploy automatizado;
> 
> Scanner de vulnerabilidades com Trivy após o push da imagem Docker;
> 
> Notificações automáticas via Discord webhook após deploy;
> 
> Estrutura de pipeline (Jenkinsfile) com todas as etapas descritas;
> 
> Arquivos de manifesto Kubernetes (deployment.yaml e service.yaml);
> 
> 📚 Esta entrega serve como base para futura implementação prática, testes e validação contínua em ambientes reais.
> 
> ✅ Toda a estrutura foi pensada com foco em CI/CD segura, modular e escalável, seguindo boas práticas DevOps e DevSecOps.


<p align="center">    
  <img src="https://github.com/user-attachments/assets/79a2e995-a1be-4192-9ded-771004ef7417" width="250">
</p>

