node {
    def branches = [:]

    branches["FRONTEND"] = {
        stage('Build frontend') {
            build job: 'minimal-react-redux', parameters: [string(name: 'BRANCH', value: 'master')], wait: true
        }
    }

    branches["BACKEND"] = {
        stage('Build backend') {
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
    }

    parallel branches

    stage('Make releasable package') {
        step([
            $class: 'CopyArtifact',
            projectName: 'minimal-react-redux',
            selector: [
                $class: 'StatusBuildSelector',
                stable: true
            ]
        ])
        archiveArtifacts artifacts: '**/*'
    }
}
