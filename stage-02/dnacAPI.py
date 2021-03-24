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
import requests
import urllib3
from requests.auth import HTTPBasicAuth
from dnacentersdk import DNACenterAPI

urllib3.disable_warnings()


######################################
# FUNCTIONS
######################################
def getAuthToken(env):
	"""
	Intent-based Authentication API call
	The token obtained using this API is required to be set as value to the X-Auth-Token HTTP Header
	for all API calls to Cisco DNA Center.
	:param env:
	:return: Token STRING
	"""
	url = '{}/dna/system/api/v1/auth/token'.format(env['base_url'])
	# Make the POST Request
	response = requests.post(url, auth=HTTPBasicAuth(env['username'], env['password']), verify=False)

	# Validate Response
	if 'error' in response.json():
		print('ERROR: Failed to retrieve Access Token!')
		print('REASON: {}'.format(response.json()['error']))

	else:
		return response.json()['Token']


def get_Dnac_Devices(env):
	url = '{}/dna/intent/api/v1/network-device'.format(env['base_url'])
	headers = {
		'x-auth-token': env['token'],
		'Content-Type': 'application/json',
		'Accept': 'application/json'
	}
	# Make the GET Request
	response = requests.get(url, headers=headers, verify=False)

	# Validate Response
	if 'error' in response.json():
		print('ERROR: Failed to retrieve Network Devices!')
		print('REASON: {}'.format(response.json()['error']))
		return []
	else:
		return response.json()['response']


def get_Dnac_Template_Projects(env):
	url = '{}/dna/intent/api/v1/template-programmer/project'.format(env['base_url'])
	headers = {
		'x-auth-token': env['token'],
		'Content-Type': 'application/json',
		'Accept': 'application/json'
	}
	# Make the GET Request
	response = requests.get(url, headers=headers, verify=False)

	# Validate Response
	if 'error' in response.json():
		print('ERROR: Failed to retrieve Network Devices!')
		print('REASON: {}'.format(response.json()['error']))
		return []
	else:
		return response.json()


def get_Dnac_Template(env, id):
	url = '{}/dna/intent/api/v1/template-programmer/template/{}'.format(env['base_url'], id)
	headers = {
		'x-auth-token': env['token'],
		'Content-Type': 'application/json',
		'Accept': 'application/json'
	}
	# Make the GET Request
	response = requests.get(url, headers=headers, verify=False)

	# Validate Response
	if 'error' in response.json():
		print('ERROR: Failed to retrieve Network Devices!')
		print('REASON: {}'.format(response.json()['error']))
		return []
	else:
		return response.json()
