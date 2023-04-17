# Importing required modules
import requests
import os
from time import sleep

# Getting environment variables
USERNAME = os.environ['USERNAME']
JENKINS_URL = os.environ['JENKINS_URL']
API_TOKEN = os.environ['API_TOKEN']
AUTH_TOKEN = os.environ['AUTH_TOKEN']

# Lambda handler function that will be called when the lambda is triggered
def lambda_handler(event, context):
    try:
        # Creating the url to trigger the jenkins job with the required parameters
        url = f"https://{USERNAME}:{API_TOKEN}@{JENKINS_URL}/job/aws-lambda-test/buildWithParameters?name=Deeksha&address=DayanandVihar"
        print(url) # Printing the url to the console
        response = requests.post(url) # Making a post request to trigger the jenkins job
        if response.status_code != 201: # Checking if the response status code is not 201 (which means success)
            print(response.status_code) # Printing the response status code to the console
    except Exception as err:
        print(err.args[0]) # Printing the error message to the console
