
from urllib import response
import requests

# Test Case 1

def test_all_posts_status():
    response = requests.get(
       "https://jsonplaceholder.typicode.com/posts",
        timeout=10
    )

    assert response.status_code == 200

# Test Case 2

def test_get_all_posts_list():
    response = requests.get(
    "https://jsonplaceholder.typicode.com/posts",
    timeout=10
    )

    assert isinstance(response.json(), list)

# Test Case 3

def test_get_posts_required_fields():
    response = requests.get(
     "https://jsonplaceholder.typicode.com/posts",
      timeout=10   
    )

    assert response.status_code == 200

    posts = response.json()

    for post in posts :
        assert "id" in post
        assert "userId" in post
        assert "title" in post
        assert "body" in post

# Test Case 4

def test_get_post_one_status():
    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts/1",
        timeout=10
    )

    assert response.status_code == 200



# Test Case 5

def test_get_post_one_fields():
    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts/1",
        timeout=10
    )
    assert response.status_code == 200
 
    posts = response.json()

    assert "id" in posts
    assert "userId" in posts
    assert "title" in posts
    assert "body" in posts

    assert posts["id"] == 1
    assert isinstance(posts["userId"], int)
    assert isinstance(posts["title"], str)
    assert isinstance(posts["body"], str)

# Test Case 6

def test_get_post_two_id():
    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts/2/",
        timeout=10
    )

    assert response.status_code == 200

    posts = response.json()

    assert posts["id"] == 2

# Test Case 7

def test_get_non_existing_post():
    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts/99999/",
        timeout=10
    )

    assert response.status_code == 404   #404 not found

    posts = response.json()

    assert posts == {}

# Test Case 8

def test_get_invalid_post_id():
    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts/abc/",
        timeout=10
    )

    print("Status Code:", response.status_code)
    print("Response:", response.text)

    assert response.status_code == 404

 # Test Case 9
  
def test_filter_posts_by_user_id(): 
    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts/",
        params={"userId":1},
        timeout=10
    ) 

    assert response.status_code == 200
    posts = response.json()

    assert isinstance(posts,list)
    assert len(posts)>0

    for post in posts:
        assert post["userId"] == 1


     # Test Case 10

    def test_invalid_http_method():
        response = requests.request(
            "TRACE"
             "https://jsonplaceholder.typicode.com/posts",
             timeout=10
        )

        print("Status Code:", response.status_code)
        print("Response:", response.text)

        assert 400 <=response.status_code<600
