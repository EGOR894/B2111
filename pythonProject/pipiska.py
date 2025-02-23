import requests

response = requests.get("https://httpbin.org/get")
print(response.content)
print(response.text)
print(f"Date Type - {type(response.text)}")
print(f"Date Type - {type(response.content)}")
🎅🏿🎅🏿🎅🏿🎅🏿🎅🏿🎅🏿
