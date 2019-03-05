from githubapimock import mock
import requests

with mock('0.0.0.0', 5000) as github:
    #r = requests.get('http://localhost:5000/issues')
    #print(r.json())
    pass
