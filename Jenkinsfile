//Jenkinsfile (Declarative Pipeline)
pipeline {
    //agent { node 'windows' }
    //agent { node 'CentOS8' }
    //agent { docker 'python:3.5.1' }
    agent { docker 'maven:3.3.3' }
    stages {
        stage('build') {
            steps {
                //bat 'cmd /c python --version'
                //sh 'python --version'
                sh 'mvn --version'
            }
        }
    }
}
