import requests
from requests.auth import HTTPBasicAuth

apiUrl = "https://www.opencve.io/api/cve?product=mongodb&cvss=high"
# response = requests.get(api_url, auth=HTTPDigestAuth('pawel', 'Lexmarkz12'))

username = 'pawel'
password = 'Lexmarkz12'

response = requests.get(apiUrl, auth = HTTPBasicAuth(username, password))
print(response.json())