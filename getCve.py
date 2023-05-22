import requests
import json
from requests.auth import HTTPBasicAuth

apiUrl = "https://www.opencve.io/api/cve?product=mongodb&cvss=critical"
username = 'pawel'
password = 'Lexmarkz12'

response = requests.get(apiUrl, auth = HTTPBasicAuth(username, password))
ids = [item["id"] for item in response.json()]

for id in ids:
    apiUrl = "https://www.opencve.io/api/cve/"+id
    response = requests.get(apiUrl, auth = HTTPBasicAuth(username, password))
    parsed_data = json.loads(response.json())
    versionEndExcluding = parsed_data['raw_nvd_data']['configurations']['nodes'][0]['cpe_match'][0]['versionEndExcluding']
    print(versionEndExcluding)
print(ids)
