import requests
from requests.auth import HTTPDigestAuth


api_url = "https://www.opencve.io/api/cve?product=mongodb&cvss=high"
response = requests.get(api_url, auth=HTTPDigestAuth('pawel', 'Lexmarkz12'))
print(response)
