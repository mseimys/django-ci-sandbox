pipeline {
    agent any 

    stages {
        stage('Setup environment') { 
            steps { 
                sh 'virtualenv env -p /usr/bin/python3'
                sh '. ./env/bin/activate'
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run unit tests') { 
            steps { 
                dir('mysite') {
                    sh 'python manage.py test'
                }
            }
        }
        stage('Lint') { 
            steps { 
                sh 'pylint mysite'
            }
        }
    }
}
