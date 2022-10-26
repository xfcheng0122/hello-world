//Jenkinsfile (Declarative Pipeline)
pipeline {
    //agent { node 'windows' }
    agent { node 'CentOS8' }
    stages {
        stage('build') {
            steps {
                //bat 'cmd /c python --version'
                sh 'python --version'
            }
        }
    }
}
