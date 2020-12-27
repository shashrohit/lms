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
                sh "echo ${WORKSPACE}"
                sh "cd C:\Users\SSingh9\.jenkins\workspace\library management system"
                sh "pytest"
            }
        }
    }
    post {
        always {
            echo 'I will always say Hello again!'
        }
    }
}
