import requests
from requests.auth import HTTPBasicAuth

apiUrl = "https://www.opencve.io/api/cve"
params = {
    "product": "mongodb"
    "cvss": "critical,high"
}
username = 'pawel'
password = 'Lexmarkz12'

response = requests.get(apiUrl, params=params, auth = HTTPBasicAuth(username, password))

print(response.json())
