"""
#Copyright (c) 2020 Cisco and/or its affiliates.
#
#This software is licensed to you under the terms of the Cisco Sample
#Code License, Version 1.1 (the "License"). You may obtain a copy of the
#License at
#
#               https://developer.cisco.com/docs/licenses
#
#All use of the material herein must be in accordance with the terms of
#the License. All rights not expressly granted by the License are
#reserved. Unless required by applicable law or agreed to separately in
#writing, software distributed under the License is distributed on an "AS
#IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
#or implied.
"""
from dnacAPI import *

######################################
# SCRIPT
######################################
# Step 1) Retrieve for Env
input_username = "XXXXX"
input_password = "XXXXX"
input_version = "XXXXX"
base_url = "XXXXX"

env = {
	'base_url': base_url,
	'username': input_username,
	'password': input_password,
	'version': input_version
}

env['token'] = getAuthToken(env)
if 'token' in env:
	print('Router Template')
	dnac_template = get_Dnac_Template(env, "")
	print('Name - {}'.format(dnac_template['name']))
	print('Content:')
	print(dnac_template['templateContent'])
	print()
	print('DNAC Network Routers:')
	complete_device_list = get_Dnac_Devices(env)
	for device in complete_device_list:
		if device['family'] == 'Routers':
			print(device['hostname'])
	# projects = get_Dnac_Template_Projects(env)
else:
	exit(1)
