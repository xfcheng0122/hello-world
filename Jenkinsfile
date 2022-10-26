//Jenkinsfile (Declarative Pipeline)
pipeline {
    //agent { node 'windows' }
    //agent { node 'CentOS8' }
    //agent { docker 'python:3.5.1' }
    //agent { docker 'maven:3.3.3' }
    //agent { docker 'node:6.3' }
    agent { docker 'ruby' }
    stages {
        stage('build') {
            steps {
                //bat 'cmd /c python --version'
                //sh 'python --version'
                //sh 'mvn --version'
                //sh 'npm --version'
                sh 'ruby --version'
            }
        }
    }
}
