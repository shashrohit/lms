pipeline{
    agent any
    stages{
        stage("Git Checkout"){
            steps{
                git 'https://github.com/shashrohit/lms.git'
            }
        }
        stage("Unit Test"){
            steps{
                echo "${WORKSPACE}"
                bat "docker build . -t lms:${BUILD_NUMBER}"
                bat "pytest"
            }
        }
    }
    post {
        always {
            echo 'I will always say Hello again!'
        }
    }
}
