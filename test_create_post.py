from urllib3._base_connection import _ResponseOptions
from urllib import response
import requests

#Test Case 1 Purpose: Is test mein hum check karenge ki valid data bhejne par API nayi post create karne ka successful response deti hai ya nahi.

def test_create_valid_post():
    url = "https://jsonplaceholder.typicode.com/posts"

    data = {
        "title": "My First Post",
        "body": "I am learning API testing",
        "userId": 1
    }

    response = requests.post(
        url,
        json=data,
        timeout=10
    )

    #print data
    print("Sent Data:", data)
    print("Status Code:", response.status_code)
    print("Response Data:", response.json())

    assert response.status_code == 201


#Test Case 2 Purpose: Is test case mein hum check karenge ki POST request mein jo title, body aur userId bheja hai, wahi data API ke response mein wapas aa raha hai ya nahi.response

def test_create_post_response_data():
    url="http://jsonplaceholder.typicode.com/posts"
    data={
        "title" : " My First Post ",
        "body" : "I am learning API  testing",
        "userId": 1
    }

    response = requests.post(
        url,
        json=data,
        timeout=10
    )

    assert response.status_code == 201

    post = response.json()

    print("Sent Data:", data)
    print("Response Data:", post)

    assert post["title"] == data["title"]
    assert post["body"] == data["body"]
    assert post["userId"] == data["userId"]

#Test Case 3

def test_create_post_generated_id():
    url="http://jsonplaceholder.typicode.com/posts"
    data={
        "title": "My Third Post",
        "body": "Learning Post API testing",
        "userId": 1
    }
    response = requests.post(
        url,
        json=data,
        timeout=10,
    )

    assert response.status_code == 201
    post = response.json()

    print("Response Data:", post)
    print("genrated ID:", post["id"])

#py -m pytest test_create_post.py::test_create_post_generated_id -v -s

#Test Case 4

def test_create_post_missing_title():
    url="http://jsonplaceholder.typicode.com/posts"
    data = {
        "body" : " I am learning API Testing",
        "userId" : 1
    }

    response = requests.post(
        url,
        json=data,
        timeout=10
    )
    
    print("Status Code:", response.status_code)
    print("Response Date:", response.json())

    assert response.status_code == 201

    post = response.json()

    assert "title" not in post
    assert post["body"] == data["body"]
    assert post["userId"] == data["userId"]

#Test Case 5

def test_create_post_missing_body():
    url="http://jsonplaceholder.typicode.com/posts"
    data={
        "title" : "My First Post",
        "userId" : 1
    }
    response = requests.post(
        url,
        json=data,
        timeout=10
    )
    print("Status Code:", response.status_code)
    print("Response Data:", response.text)

    assert response.status_code == 201
    post = response.json()

    assert "body" not in post
    assert post ["title"] == data["title"]
    assert post ["userId"] == data["userId"]
    
#Test Case 6

def test_create_post_empty_title():
      url="http://jsonplaceholder.typicode.com/posts"
      data= {
        "title" : "",
        "body" : "I am learning API testing",
        "userId" : 1
      }

      response = requests.post(
        url,
        json=data,
        timeout=10
      )

      print("Status Code:", response.status_code)
      print("Sent Data:", data)

      assert response.status_code == 201

      post = response.json()
      print("Response Data:", post)

      assert "title" in post
      assert post["title"] == ""
      assert post["body"] == data["body"]
      assert post["userId"] == data["userId"]

#Test Case 7

def test_create_post_invalid_user_id():
    url="http://jsonplaceholder.typicode.com/posts"
    data= {
        "title" : "My First Post",
        "body" : "I am learning API testing",
        "userId" : "abc"
      }

    response = requests.post(
        url,
        json=data,
        timeout=10
      )
    
    post = response.json()
    print("Sent Data:", data)
    print("Response Data:", post)
    print("Status Code:", response.status_code)

    assert response.status_code == 201
    assert post["userId"] == data["userId"]
    assert isinstance(post["userId"], str)
    
