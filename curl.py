import requests

headers = {
    # Already added when you pass json= but not when you pass data=
    # 'Content-Type': 'application/json',
}

json_data = {
    'name': 'dummy',
    'age': 21,
    'friends': [
        'dummy1',
        'dummy2',
        'dummy3',
    ],
    'is_man': False,
}

response = requests.post('http://127.0.0.1:5000/try_rest', headers=headers, json=json_data)
response_json = response.json()
friends = response_json['response_json']['friends']
for i in  friends:
    print(i)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"name":"dummy", "age":21, "friends":["dummy1", "dummy2", "dummy3"], "is_man":false}'
#response = requests.post('http://127.0.0.1:5000/try_rest', headers=headers, data=data)