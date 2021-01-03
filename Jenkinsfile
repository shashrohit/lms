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
                publishHTML (target : [allowMissing: false,
                 alwaysLinkToLastBuild: true,
                 keepAll: true,
                 reportDir: 'unit_tests\reports',
                 reportFiles: 'coverage.html',
                 reportName: 'Unit Tests Report',
                 reportTitles: 'Unit Tests Report'])
            }
        }
        stage('Sonarqube') {
            environment {
                scannerHome = tool 'SonarQubeScanner'
            }
            steps {
                catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
                    withSonarQubeEnv('sonarqube') {
                        bat "${scannerHome}/bin/sonar-scanner"
                    }
                }
                timeout(time: 10, unit: 'MINUTES') {
                    waitForQualityGate abortPipeline: true
                }
            }
        }
        stage("API Test"){
            steps{
                script{
                    catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
                        bat "docker-compose -f api-test.yml up --build --exit-code-from api_tests"
                    }
                }
                publishHTML (target : [allowMissing: false,
                 alwaysLinkToLastBuild: true,
                 keepAll: true,
                 reportDir: 'api_tests\reports',
                 reportFiles: 'index.html',
                 reportName: 'API Tests Report',
                 reportTitles: 'API Tests Report'])
            }
        }

    }
    post {
        always {
            echo 'I will always say Hello again!'
        }
    }
}
