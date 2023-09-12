Person API Documentation

This documentation provides details on how to use the Simple Person API.

Table of Contents
- [Standard Formats](#standard-formats)
- [Endpoints](#endpoints)
- [Sample Usage](#sample-usage)
- [Limitations and Assumptions](#limitations-and-assumptions)
- [Setting Up and Deploying](#setting-up-and-deploying)

Standard Formats

Request Format

All requests should be made using JSON format. For example, when creating a new person:

```json
{
    "name": "John Doe"
}

Response Format

Responses from the API will be in JSON format. For example, a successful creation response:

{
    "message": "Person created successfully"
}

**Endpoints**

    POST /api: Create a new person.
    GET /api/{user_id}: Retrieve details of a person.
    PUT /api/{user_id}: Update the details of a person.
    DELETE /api/{user_id}: Delete a person.

Sample Usage
Creating a New Person

To create a new person, make a POST request to /api with a JSON body containing the person's name.
Retrieving a Person

To retrieve the details of a person, make a GET request to /api/{user_id}.
Updating a Person

To update the details of a person, make a PUT request to /api/{user_id} with a JSON body containing the updated information.
Deleting a Person

To delete a person, make a DELETE request to /api/{user_id}.
Setting Up and Deploying

For instructions on setting up and deploying the API, please refer to the README.md file.
