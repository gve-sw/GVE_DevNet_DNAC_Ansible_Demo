# GVE_DevNet_DNAC_Ansible_Demo

## Contacts
* Alexander Hoecht

## Solution Components
* Ansible
* Cisco DNA-Center
* Cisco Network Devices

## Installation/Configuration
Installation:
```
# Create Virtual Environment (MacOS)
python3 -m venv VirtualEnvironment
source VirtualEnvironment/bin/activate
pip install --upgrade pip
pip install -r demoRequirements.txt
```
Configuration:
```yaml
# STAGE - 00
# In the inventory file, properly define any variables set to XXXXX

[lab_router_a:vars]
hostname=XXXXX
ansible_user=XXXXX
ansible_ssh_pass=XXXXX
ansible_connection=network_cli
ansible_network_os=ios
ansible_python_interpreter=python3
```
```yaml
# STAGE - 01
# In the hosts.yml file, properly define any variables set to XXXXX

demo_server:
      dnac_host: XXXXX
      dnac_port: 443
      dnac_username: XXXXX
      dnac_password: XXXXX
      dnac_version: 2.1.1
      dnac_verify: False
```
```python
# STAGE - 02
# In the demo.py file, properly define any variables set to XXXXX

input_username = "XXXXX"
input_password = "XXXXX"
input_version = "XXXXX"
base_url = "XXXXX"
```


## Usage
Stage-00:
```
ansible-playbook -i stage-00/ansible/inventory stage-00/ansible/apply_demo_csr_template.yml
```
Stage-01:
```
ansible-playbook -i stage-01/ansible/hosts.yml stage-01/ansible/output_dnac_project_info.yml
```
Stage-02:
```
python3 stage-02/demo.py
```



# Screenshots

![/IMAGES/0image.png](/IMAGES/0image.png)

### LICENSE

Provided under Cisco Sample Code License, for details see [LICENSE](LICENSE.md)

### CODE_OF_CONDUCT

Our code of conduct is available [here](CODE_OF_CONDUCT.md)

### CONTRIBUTING

See our contributing guidelines [here](CONTRIBUTING.md)

#### DISCLAIMER:
<b>Please note:</b> This script is meant for demo purposes only. All tools/ scripts in this repo are released for use "AS IS" without any warranties of any kind, including, but not limited to their installation, use, or performance. Any use of these scripts and tools is at your own risk. There is no guarantee that they have been through thorough testing in a comparable environment and we are not responsible for any damage or data loss incurred with their use.
You are responsible for reviewing and testing any scripts you run thoroughly before use in any non-testing environment.
