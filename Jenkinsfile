pipeline {
    agent any

    stages {
        stage('Enable all scripts to be executable') {
            steps {
                sh 'chmod +x ./script/*'
            }
        }
        stage('Get the envinronment ready') {
            steps {
                sh './script/before_installation.sh'
                sh './script/installation.sh'
            }
        }
        stage('Run the application') {
            steps {
                sh 'sudo systemctl restart flask.service'
            }
        }
    }
}