pipeline {
    agent any
    def branches = [:]

    stages {
        branches["FRONTEND"] = {
            build job: 'minimal-react-redux', parameters: [string(name: 'BRANCH', value: 'master')], wait: true
            step([
                    $class: 'CopyArtifact',
                    projectName: 'minimal-react-redux',
                    selector: [
                        $class: 'StatusBuildSelector',
                        stable: false
                    ]
            ])
        }

        branches["BACKEND"] = {
            sh("""
            virtualenv env -p /usr/bin/python3
            . ./env/bin/activate
            pip install -r requirements.txt
            """)
            dir('mysite') {
                sh("""
                . ../env/bin/activate
                python manage.py test
                """)
            }
            sh("""
            . ./env/bin/activate
            pylint mysite | tee pylint.log
            """)
        }

        stage('Build') {
            parallel branches
        }

        stage('Make releasable package') {
            steps {
                archiveArtifacts artifacts: '**/*'
            }
        }
    }
}
