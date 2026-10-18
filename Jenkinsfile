pipeline {
    agent any
    environment {
        IMAGE_NAME = 'ahmadnurabid/simple-app'
        REGISTRY_CREDENTIALS = 'dockerhub-credentials'
    }
    stages {
        stage('Checkout') {
            steps {
                echo 'Melakukan checkout dari SCM...'
                checkout scm
            }
        }
        stage('Build') {
            steps {
                echo 'Mulai build aplikasi'
                bat 'echo Build selesai'
            }
        }
        stage('Build Docker Image') {
            steps {
                echo 'Membangun Docker image...'
                bat "\"C:\\Program Files\\Docker\\Docker\\resources\\bin\\docker.bat\" build -t %IMAGE_NAME%:%BUILD_NUMBER% ."
                echo "Image berhasil dibuat: %IMAGE_NAME%:%BUILD_NUMBER%"
            }
        }
        stage('Push Docker Image') {
            steps {
                echo 'Push image ke Docker Hub...'
                withCredentials([usernamePassword(credentialsId: REGISTRY_CREDENTIALS, usernameVariable: 'USER', passwordVariable: 'PASS')]) {
                    bat "\"C:\\Program Files\\Docker\\Docker\\resources\\bin\\docker.bat\" login -u %USER% -p %PASS%"
                    bat "\"C:\\Program Files\\Docker\\Docker\\resources\\bin\\docker.bat\" push %IMAGE_NAME%:%BUILD_NUMBER%"
                    bat "\"C:\\Program Files\\Docker\\Docker\\resources\\bin\\docker.bat\" tag %IMAGE_NAME%:%BUILD_NUMBER% %IMAGE_NAME%:latest"
                    bat "\"C:\\Program Files\\Docker\\Docker\\resources\\bin\\docker.bat\" push %IMAGE_NAME%:latest"
                }
            }
        }
    }
    post {
        always {
            echo 'Selesai build'
        }
    }
}
