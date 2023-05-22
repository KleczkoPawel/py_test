import requests
from requests.auth import HTTPBasicAuth

apiUrl = "https://www.opencve.io/api/cve?product=mongodb&cvss=critical"

username = 'pawel'
password = 'Lexmarkz12'

response = requests.get(apiUrl, auth = HTTPBasicAuth(username, password))

print(response.json())

CVE-2017-15535
CVE-2020-7610
VE-2022-48282
CVE-2020-7923"