import requests

apiUrl = "https://www.opencve.io/api/cve?product=mongodb&cvss=high"
# response = requests.get(api_url, auth=HTTPDigestAuth('pawel', 'Lexmarkz12'))

username = 'pawel'
password = 'Lexmarkz12'

session = requests.Session()
response = session.post(
    apiUrl,
    json={'identifier': username, 'password': password},
    headers={'VERSION': '2'},
)
response.raise_for_status()  # if not a 2xx response, raise an exception
