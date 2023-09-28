pipeline {
    agent any
    stages {
        stage('Build'){
            steps {
                sh "apt get docker" || true
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
