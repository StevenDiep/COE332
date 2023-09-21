import requests
import json

res = requests.get('http://127.0.0.1:5000/degrees')

print(res.status_code)
#print(res.content)
print(res.json())
print('=======================')

