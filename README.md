# Jenkins Job Trigger Lambda Function


This lambda function that triggers a Jenkins job with required parameters by making a POST request to the Jenkins API. It is designed to run on the AWS Lambda platform and requires the following environment variables to be set:

- **USERNAME:** The username for authenticating with the Jenkins API.
- **JENKINS_URL:** The URL for the Jenkins server.
- **API_TOKEN:** The API token for authenticating with the Jenkins API.
- **AUTH_TOKEN:** The authentication token for the Lambda function.

### **How to Use**
To use this lambda function, follow these steps:

- Clone this repository to your local machine.

- Set up the required environment variables on your AWS Lambda platform. You can do this using the AWS Lambda console or CLI.

- Deploy the lambda function to your AWS account. You can do this using the AWS Lambda console or CLI.

- Once the function is deployed, you can trigger it by calling it with the required event payload.

### **Event Payload**

This lambda function does not require any specific event payload. You can pass any payload or leave it empty.

### **Output**
This lambda function prints some information to the console for debugging purposes. Specifically, it prints the URL used to trigger the Jenkins job and the status code of the API response if it is not 201 (which means success). If an error occurs, it also prints the error message to the console.