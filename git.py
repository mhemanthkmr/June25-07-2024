import requests

url = "https://github.com/krithi0301/gitkrith01.git"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
