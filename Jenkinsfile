pipeline {
    agent any
    stages {
        stage('Build'){
            steps {
                sh "sudo apt update"
                sh "sudo apt install -y curl"
                sh "curl https://get.docker.com | bash"
                sh "sudo usermod -aG docker $(whoami)"
            }
        }
        stage('Test'){
            steps {
                sh "pwd" 
            }
        }
        stage('Deploy'){
          steps {
            sh "ls" 
            }
        }
    }
}    
