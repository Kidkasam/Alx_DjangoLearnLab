
import requests
import json

BASE_URL = "http://127.0.0.1:8000/api/books_all/"

def test_crud():
    # 1. List (GET)
    response = requests.get(BASE_URL)
    print(f"List (GET) Status: {response.status_code}")
    print(f"List Result: {response.json()}")

    # 2. Create (POST)
    new_book = {"title": "New Book", "author": "New Author"}
    response = requests.post(BASE_URL, data=new_book)
    print(f"Create (POST) Status: {response.status_code}")
    print(f"Create Result: {response.json()}")
    
    if response.status_code == 201:
        book_id = response.json()['id']
        
        # 3. Retrieve (GET)
        response = requests.get(f"{BASE_URL}{book_id}/")
        print(f"Retrieve (GET) Status: {response.status_code}")
        print(f"Retrieve Result: {response.json()}")

        # 4. Update (PUT)
        updated_book = {"title": "Updated Book", "author": "Updated Author"}
        response = requests.put(f"{BASE_URL}{book_id}/", data=updated_book)
        print(f"Update (PUT) Status: {response.status_code}")
        print(f"Update Result: {response.json()}")

        # 5. Delete (DELETE)
        response = requests.delete(f"{BASE_URL}{book_id}/")
        print(f"Delete (DELETE) Status: {response.status_code}")
        
        # Verify Deletion
        response = requests.get(f"{BASE_URL}{book_id}/")
        print(f"Verify Delete (GET) Status: {response.status_code}")
    else:
        print("Failed to create book, skipping retrieval, update, and delete tests.")

if __name__ == "__main__":
    test_crud()
