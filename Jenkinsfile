pipeline {
    agent any
    options {
        skipStagesAfterUnstable()
    }
    stages {
        stage('Build') {
            steps {
                sh 'python -m py_compile ources/add2vals.py sources/calc.py'
                stash(name: 'compiled-results', includes: 'sources/*.py*')
            }
        }
        // stage('Test') {
        //     agent {
        //         docker {
        //             image 'qnib/pytest'
        //         }
        //     }
        //     steps {
        //         sh 'py.test --junit-xml test-reports/results.xml sources/test_calc.py'
        //     }
        //     post {
        //         always {
        //             junit 'test-reports/results.xml'
        //         }
        //     }
        // }
    }
}