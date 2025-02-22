pipeline {
    agent any

    stages {
        // stage('Clone Repo') {
        //     steps {
        //         git credentialsId: 'df2c59f5-3b0d-4f0d-971e-927fc5bd0afd', url: 'https://github.com/aakash-tsx/testing_auto_versioning.git'
        //     }
        // }
        stage('Run Model') {
            steps {
                sh 'python test.py'  // Runs your ML script
            }
        }
        
    }
}
