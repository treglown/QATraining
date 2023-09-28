pipeline {
    agent any
    stages {
        stage('Build'){
            steps {
                sh "sudo apt update 
                sudo apt install -y curl
                curl https://get.docker.com | bash
                sudo usermod -aG docker $(jenkins)"
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
