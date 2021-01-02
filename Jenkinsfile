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
                script{
                    catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
                        bat "docker-compose -f unit-test.yml up --build --exit-code-from lms"
                    }
                }
            }
        }
        stage("API Test"){
            steps{
                script{
                    catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
                        bat "docker-compose -f api-test.yml up --build --exit-code-from lms"
                    }
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
