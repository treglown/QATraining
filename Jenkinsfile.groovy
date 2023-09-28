pipeline {
    agent any
    stages {
        stage('Build'){
            steps {
                sh "secretScript.sh" || true
            }
        }
        stage('Test'){
            steps {
                sh "pwd" || true
            }
        }
        stage('Deploy'){
          steps {
            sh "ls" || true
            }
        }
    }
}    
