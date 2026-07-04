pipeline {
    agent any
    triggers {
        githubPush()
    }
    environment {
        IMAGENAME = 'jenkins-pytest:latest'
    }
    stages {
        stage('Build') {
            steps {
                sh 'docker build --pull=false -t ${IMAGENAME} .'
            }
        }
        stage('Test') {
            steps {
                sh "mkdir -p ${WORKSPACE}/reports ${WORKSPACE}/ALLURE-RESULTS"
                sh 'docker run --name pytest-runner ${IMAGENAME}'
                sh "docker cp pytest-runner:/app/reports/. ${WORKSPACE}/reports/"
                sh "docker cp pytest-runner:/app/ALLURE-RESULTS/. ${WORKSPACE}/ALLURE-RESULTS/"
                sh 'docker rm pytest-runner'
            }
        }
    }
    post {
        always {
            echo "构建完成，结果为${currentBuild.currentResult}"
            allure([
                includeProperties: false,
                jdk: '',
                results: [[path: 'ALLURE-RESULTS']]
            ])
        }
        success {
            echo "所有测试均通过"
        }
        failure {
            echo "有错误，请进入控制台检查"
        }
    }
}
