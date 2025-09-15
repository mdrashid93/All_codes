import requests,json

payload=json.dumps({
    "age":10,
    "sex":"f"
})
response=requests.put("url",data=payload)
print(response.json())
