pipeline {
    agent any
    stages {
        stage('Job: clean up containers'){
            steps {
                sh "docker rm -f $(docker ps -aq)" || true
            }
        }
        stage('Job: Build'){
            steps {
                sh "sh build.sh"
            }
        }
    }
}    
