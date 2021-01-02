pipeline{
    agent any
    stages{
        stage("Git Checkout"){
            steps{
                git 'https://github.com/shashrohit/lms.git'
            }
        }
        stage("Unit Tests"){
            steps{
             catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
                    bat "docker-compose -f unit-test.yml up --build"
                }
            }
        }
    }
    post {
        always {
            echo 'I will always say Hello again!'
        }
    }
}
