#PUT API

from urllib import response
import requests

#Test Case 1

def test_put_post_status():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    data = {
        "id" : 1,
        "title" : " Updated POST title",
        "body": "I am learning PUT API testing",
        "userId" : 1 
    }

    response = requests.put(
        url,
        json=data,
        timeout=10
    )

    post = response.json()

    print("Sent Data:", data)
    print("Response Data:", post)
    print("Status code:", response.status_code)

    assert response.status_code == 200

#Test Case 2

def test_put_updated_fields():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    data = {
        "id" : 1,
        "title": "My Updated title",
        "body": "I am learning PUT API testing",
        "userId": 1
    }
    response = requests.put(
        url,
        json=data,
        timeout=10
    )
    assert response.status_code == 200
    post = response.json()

    print("Sent Data:", data)
    print("Response Data:", post)
    print("Status Code:", response.status_code)

    assert post["id"] == data["id"]
    assert post["title"] == data["title"]
    assert post["body"] == data["body"]
    assert post["userId"] == data["userId"]

#Test Case 3

def test_put_response_structure():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    data = {
        "id" : 1,
        "title" : "Updated POST API testing",
        "userId" : 1,
        "body" : "I am learning PUT API testing"
    }     

    response = requests.put(
        url,
        json=data,
        timeout=10
    )
    assert response.status_code == 200
    post = response.json()
    print("Sent Data :", data)
    print("Response Data:", post)
    print("Status Code:", response.status_code)

    assert isinstance(post,dict)

    assert "id" in post
    assert "userId" in post
    assert "title" in post
    assert "body" in post

    assert isinstance(post["id"], int)
    assert isinstance(post["userId"], int)
    assert isinstance(post["title"], str)
    assert isinstance(post["body"], str)


#PATCH API

#Test Case 1

def test_patch_post_title():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    data = {
        "title" : "My New Updated Title"
    }
    response = requests.patch(
        url,
        json=data,
        timeout=10
    )
    assert response.status_code == 200
    post = response.json()

    print("Sent Data:", data)
    print("Response Data:", post)
    print("Status Code:", response.status_code)

    assert post ["title"] == data["title"]