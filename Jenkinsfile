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
                script{
                    catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
                        bat "echo %ERRORLEVEL%"
                        bat "docker-compose -f unit-test.yml up --build -exit-code-from lms"
                        bat "echo %ERRORLEVEL%"
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
