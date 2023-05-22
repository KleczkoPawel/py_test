import requests
from requests.auth import HTTPBasicAuth

apiUrl = "https://www.opencve.io/api/cve?product=mongodb&cvss=high"

username = 'pawel'
password = 'Lexmarkz12'

# response = requests.get(apiUrl, auth = HTTPBasicAuth(username, password))
session = requests.Session()
session.auth(username,password)
response = session.get(apiUrl)
print(response.json())