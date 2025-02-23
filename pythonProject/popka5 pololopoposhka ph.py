import requests
response = requests.post("https://httpbin.org/post", data="Test data", headers={"hi":"Test title"})
print(response.text)