pipeline {
    agent any 

    stages {
        stage('Setup environment') { 
            steps { 
                bash 'virtualenv env -p /usr/bin/python3'
                bash '. ./env/bin/activate'
                bash 'pip install -r requirements.txt'
            }
        }
        stage('Run unit tests') { 
            steps { 
                dir('mysite') {
                    bash 'python manage.py test'
                }
            }
        }
        stage('Lint') { 
            steps { 
                bash 'pylint mysite'
            }
        }
    }
}
