import requests

url = "https://jsonplaceholder.typicode.com/posts"

payload = {
    'title' : 'Hello from Python',
    'body' : 'This is test program',
    'userId' : 1,
    'id' : 101
}

response = requests.post(url, json=payload)

# print(response.status_code)
# print(response.json())


url = "http://127.0.0.1:5000/"

response = requests.get(url).json()

print(response)


