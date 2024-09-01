#Working with APIs
import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Request failed with status code: {response.status_code}")

#Handling Query Parameters
url = "https://jsonplaceholder.typicode.com/posts"

# Query parameters
params = {
    "userId": 1
}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    for post in data:
        print(post)
else:
    print(f"Request failed with status code: {response.status_code}")

#POST Request
url = "https://jsonplaceholder.typicode.com/posts"

# Data to send in the POST request
payload = {
    "title": "foo",
    "body": "bar",
    "userId": 1
}

# Sending a POST request
response = requests.post(url, json=payload)

if response.status_code == 201:
    data = response.json()
    print("Data created successfully:", data)
else:
    print(f"Request failed with status code: {response.status_code}")

#Error Handling
try:
    response = requests.get("https://jsonplaceholder.typicode.com/invalid_endpoint")
    response.raise_for_status()  
except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")
except Exception as err:
    print(f"Other error occurred: {err}")

#Processing API Data
url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    from collections import Counter

    user_posts = Counter([post['userId'] for post in data])
    print("Number of posts by each user:", user_posts)
else:
    print(f"Request failed with status code: {response.status_code}")

#Pagination
url = "https://jsonplaceholder.typicode.com/posts"

params = {
    "_page": 1, 
    "_limit": 10 
}

while True:
    response = requests.get(url, params=params)
    data = response.json()

    if not data:
        break 

    for post in data:
        print(post)

    params["_page"] += 1 
