import time
import requests

# Function to load the GitHub token from a file (token.txt)
def load_github_token():
    try:
        with open('token.txt', 'r') as file:
            return file.read().strip()
    except FileNotFoundError:
        print("Error: 'token.txt' file not found!")
        return None

# Function to get the list of Codespaces and their statuses
def get_codespace_status(token):
    url = 'https://api.github.com/user/codespaces'
    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github+json'
    }
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        codespaces = response.json()['codespaces']
        if codespaces:
            return codespaces[0]['name'], codespaces[0]['state']
        else:
            print("No Codespaces found.")
            return None, None
    else:
        print(f"Error fetching codespaces: {response.status_code} - {response.text}")
        return None, None

# Function to start the Codespace by name
def start_codespace(codespace_name, token):
    if codespace_name is None:
        print("No valid codespace found to start.")
        return
    
    url = f'https://api.github.com/user/codespaces/{codespace_name}/start'
    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github+json'
    }
    response = requests.post(url, headers=headers)
    
    if response.status_code == 201:
        print("Codespace started successfully.")
    elif response.status_code == 200:
        print("Codespace is already running or started successfully.")
    elif response.status_code == 404:
        print("Codespace not found. Please ensure the codespace exists and the name is correct.")
    else:
        print(f"Error starting codespace: {response.status_code}")

# Function to continuously monitor and ensure the Codespace is running
def monitor_codespace(token):
    while True:
        codespace_name, status = get_codespace_status(token)
        
        if status == 'Shutdown':
            print(f"Codespace '{codespace_name}' is shutdown. Attempting to start it...")
            start_codespace(codespace_name, token)
        elif status == 'Running':
            print(f"Codespace '{codespace_name}' is running.")
        else:
            print(f"Codespace '{codespace_name}' is in state: {status}")
        
        time.sleep(6)  # Check every minute

if __name__ == "__main__":
    print("This file made by @X9HYDRA")
    print("This file made by @X9HYDRA")
    print("This file made by @X9HYDRA")
    print("This file made by @X9HYDRA") # Printed only once when the script is executed
    
    # Load the GitHub token from the token.txt file
    GITHUB_TOKEN = load_github_token()
    
    if GITHUB_TOKEN:
        monitor_codespace(GITHUB_TOKEN)
    else:
        print("Failed to load GitHub token. Please check token.txt file.")
