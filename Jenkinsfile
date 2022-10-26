//Jenkinsfile (Declarative Pipeline)
pipeline {
    //agent { node 'windows' }
    //agent { node 'CentOS8' }
    agent { docker 'python:3.5.1' }
    stages {
        stage('build') {
            steps {
                //bat 'cmd /c python --version'
                sh 'python --version'
            }
        }
    }
}
