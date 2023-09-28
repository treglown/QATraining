pipeline {
    agent any
    stages {
        stage('Build'){
            steps {
                sh "sh secretScript.sh" 
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
