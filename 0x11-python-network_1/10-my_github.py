#!/usr/bin/python3
"""
Python script that takes your Github credentials (username and password)
and uses the Github API to display your id
"""
import requests
import sys

def get_github_user_id(username, personal_access_token):
    # Define the GitHub API URL for the authenticated user
    api_url = f'https://api.github.com/user'

    # Create a Basic Authentication header with your username and personal access token
    auth_header = (username, personal_access_token)

    try:
        # Send a GET request to the GitHub API with Basic Authentication
        response = requests.get(api_url, auth=auth_header)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            user_data = response.json()
            user_id = user_data.get('id')
            if user_id:
                return user_id
            else:
                print("Failed to retrieve user ID.")
        else:
            print(f"Request failed with status code {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <username> <personal_access_token>")
    else:
        username = sys.argv[1]
        personal_access_token = sys.argv[2]
        user_id = get_github_user_id(username, personal_access_token)
        if user_id:
            print(f"Your GitHub User ID is: {user_id}")

