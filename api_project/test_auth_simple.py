
import requests

BASE_URL = "http://127.0.0.1:8000/api/books_all/"
TOKEN_URL = "http://127.0.0.1:8000/api/api-token-auth/"

def test_auth():
    # 1. Access without token
    print("Testing access without token...")
    response = requests.get(BASE_URL)
    print(f"Status Code: {response.status_code}") # Expect 401
    
    # 2. Get Token
    print("\nObtaining token...")
    auth_data = {'username': 'testuser', 'password': 'testpass123'}
    token_response = requests.post(TOKEN_URL, data=auth_data)
    print(f"Token Response Status: {token_response.status_code}")
    
    if token_response.status_code == 200:
        token = token_response.json()['token']
        print(f"Token obtained: {token}")
        
        # 3. Access with token
        print("\nTesting access with token...")
        headers = {'Authorization': f'Token {token}'}
        auth_response = requests.get(BASE_URL, headers=headers)
        print(f"Status Code: {auth_response.status_code}") # Expect 200
        print(f"Response: {auth_response.json()}")
    else:
        print("Failed to obtain token")

if __name__ == "__main__":
    test_auth()
