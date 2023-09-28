pipeline {
    agent any
    stages {
        stage('Build'){
            steps {
                sh "sudo apt-get update" || true
                sh "curl -fsSL https://download.docker.com/linux/ubuntu/gpg"
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
