pipeline {
  agent {
    docker {
      image 'python:3.9.0'
    }

  }
  stages {
    stage('Build Demo Env') {
      steps {
        echo 'Creating Virtual Environment'
        sh 'pip3 install --upgrade pip'
        sh 'pip3 install -r demoRequirements.txt'
        sh 'ansible-galaxy collection install cisco.dnac'
      }
    }

    stage('Stage-00') {
      steps {
        dir(path: 'stage-00/ansible') {
          sh 'ansible-playbook -i inventory apply_demo_csr_template.yml'
        }

      }
    }

    stage('Stage-01') {
      steps {
        dir(path: 'stage-01/ansible') {
          sh 'ansible-playbook -i hosts.yml output_dnac_project_info.yml '
        }

      }
    }

    stage('Stage-02') {
      steps {
        dir(path: 'stage-02') {
          sh 'python3 demo.py'
        }

      }
    }

  }
}