import requests

# Define the URL
url = "https://api.filutils.com/api/v2/miner/f01697248"

# Define the headers
headers = {
    'accept': 'application/json',
}

# Send a POST request to the API
response = requests.post(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    # Print the response
    print(response.json())
else:
    print(f"Request failed with status code {response.status_code}")
