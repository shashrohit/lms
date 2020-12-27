pipeline{
    agent {label 'docker'}
    stages{
        stage("Git Checkout"){
            steps{
                git 'https://github.com/shashrohit/lms.git'
            }
        }
        stage("Unit Test"){
            steps{
                sh "pytest"
            }
        }
    }
    }
}