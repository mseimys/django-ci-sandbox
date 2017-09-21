pipeline {
    agent any

    stages {
        stage('Build frontend') {
            steps {
                build 'minimal-react-redux', parameters: [string(name: 'BRANCH', value: 'master')]
                step([
                        $class: 'CopyArtifact',
                        filter: '*',
                        projectName: 'minimal-react-redux',
                        selector: [
                            $class: 'StatusBuildSelector',
                            stable: false
                        ]
                ])
            }
        }
        stage('Setup environment') {
            steps {
                sh("""
                virtualenv env -p /usr/bin/python3
                . ./env/bin/activate
                pip install -r requirements.txt
                """)
            }
        }
        stage('Run unit tests') {
            steps {
                dir('mysite') {
                    sh("""
                    . ../env/bin/activate
                    python manage.py test
                    """)
                }
            }
        }
        stage('Lint') {
            steps {
                sh("""
                . ./env/bin/activate
                pylint mysite | tee pylint.log
                """)
                archiveArtifacts artifacts: 'pylint.log'
            }
        }
        stage('Build releasable package') {
            steps {
                archiveArtifacts artifacts: '**'
            }
        }
    }
}
