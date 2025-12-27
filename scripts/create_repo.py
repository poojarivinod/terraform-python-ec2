"""
This script creates a GitHub repository using the GitHub API.
It requires a personal access token with the necessary permissions.
"""

import requests
import json # json will be installed along with the python
from dotenv import dotenv_values # search in google as "pypi" --> PyPI · The Python Package Index --> In search, type as "python-dotenv" --> click on python-dotenv --> here we have example how to use "python-dotenv" 

config = dotenv_values(r".env") # it is in same folder of script, so we given the (.env)

# Configuration
github_token = config['github_token'] # this command get the github_token from the .env
user_name = 'poojarivinod' #github username
repo_name = 'terraform-python-ec2-1' # repo name we want to create
description = 'This repo is to discuss about python usecases'

# search in google as "github api" --> GitHub REST API documentation
# GitHub API URL for creating a repository within an organization
url = f'https://api.github.com/user/repos'

# Headers and payload
headers = {
    'Authorization': f'token {github_token}',
    'Accept': 'application/vnd.github+json',
}
# this is the data we are sending to create repo
payload = {
    'name': repo_name,
    'description': description,
    'private': False  # Set to True if you want to create a private repository
}

# Make the request to create a repository
response = requests.post(url, headers=headers, data=json.dumps(payload))

# Check the response
if response.status_code == 201: # 201, created. it means success
    print(f'Repository {repo_name} created successfully within {user_name}.')
    print(f'Repository URL: {response.json()["html_url"]}')
else:
    print(f'Failed to create repository in {user_name}. Status code: {response.status_code}')
    print(f'Response: {response.text}')
