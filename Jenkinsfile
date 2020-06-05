pipeline {
    agent any

    stages {
        stage('Enable all scripts to be executable') {
            steps {
                sh 'chmod +x ./script/*'
            }
        }
        
        }
        stage('Run the application') {
            steps {
                sh './script/docker.sh'
            }
        }
    }
