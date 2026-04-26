pipeline {
    agent any

    stages {

        stage('Clone Repository') {
            steps {
                git 'https://github.com/VPatil3155/event-registration.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t event-registration .'
            }
        }

        stage('Run Container') {
            steps {
                bat 'docker run -d -p 5000:5000 event-registration'
            }
        }

        stage('Test Application') {
            steps {
                echo 'Application deployed successfully'
            }
        }
    }
}