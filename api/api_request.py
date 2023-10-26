import requests

url = 'http://127.0.0.1:8000/api/v1/customerdetails/'  # Replace with your API URL
token = '1234567890bcdefgh'  # Replace with your actual authentication token

headers = {
    'Authorization': f'Token {token}',  # Modify based on the API's authentication method
}

response = requests.get(url, headers=headers)

# Handle the response as needed
