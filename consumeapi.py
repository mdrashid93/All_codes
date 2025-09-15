import requests

url=""

age=15
sex="f"

response=requests.get(f"url=age={age}&sex={sex}")
output=response.json()
print(output)`

response=requests.get(f"{name}{age}")
o=response.json()
print(o)