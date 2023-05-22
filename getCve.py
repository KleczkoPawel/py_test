import requests

api_url = "https://www.opencve.io/api/cve?product=mongodb&cvss=high"
response = requests.get(api_url)
print(response)
