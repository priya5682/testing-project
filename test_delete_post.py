from urllib import response
import requests

#Test Case 1
# Check DELETE request returns status 200.

def test_delete_post_status():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.delete(
        url,
        timeout=10
    )

    print("Status Code:", response.status_code)
    print("Response Data:", response.text)

    assert response.status_code == 200


#Test Case 2  ( Delete Only one data)

def test_delete_one_post_data_status():
    url = "https://jsonplaceholder.typicode.com/posts/1"

    data = {
    "title": ""
}

    response = requests.delete(
        url,
        timeout=10
    )

    print("Status Code:", response.status_code)
    print("Response Data:", response.text)

    assert response.status_code == 200


# Test Case 2
# Verify DELETE response is empty {}.

def test_delete_post_response():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    
    response = requests.delete( url, timeout=10)

    assert response.status_code == 200
    post = response.json()

    print("Status Code:", response.status_code)
    print("Response Data:", post)

    assert isinstance(post, dict)
    assert post == { }


#Test Case 3        #
# Check post remains accessible after simulated DELETE.

def test_get_after_delete_simulation():
    url = "https://jsonplaceholder.typicode.com/posts/1"

    # step 1: Delete requests
    delete_response = requests.delete(
        url,
        timeout=10
    )

    print("Delete Status Code:", delete_response.status_code)
    assert delete_response.status_code == 200

    # step 2: GET request after DELETE
    get_response = requests.get(
        url,
        timeout=10
    )
    print("GET Status Code:", get_response.status_code)
    print("GET Response Data:", get_response.json())

    assert get_response.status_code == 200
    post = get_response.json()
    assert post["id"] == 1

    #py -m pytest test_delete_post.py::test_get_after_delete_simulation -v -s