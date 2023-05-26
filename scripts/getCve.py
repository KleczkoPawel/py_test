import requests
import json
from requests.auth import HTTPBasicAuth
import sys

mongoUrl = sys.argv[1]
mongodbVersion = sys.argv[2]
#mongoUrl = "https://www.opencve.io/api/cve?product=mongodb&cvss="
#postgresqlUrl = "https://www.opencve.io/api/cve?product=postgresql&cvss="
#mysqlUrl = "https://www.opencve.io/api/cve?product=mysql&cvss="
#mongodbVersion = "5.0.2".split(".")
# postgresqlVersion = "10.1".split(".")
#mysqlVersion = "3.3.0".split(".")
username = 'pawel'
password = '5ZmZ5GGs9S'

def countDatabaseVulnerabilities(url, checkVersion):
    url += "&cvss="
    checkVersion = checkVersion.split(".")
    serverity = ["high","critical"]
    numberOfVulnerabilities = 0
    ids = []

    # Get all CVE-s for all declared serverities
    for endpoint in serverity:
        response = requests.get(url+endpoint, auth = HTTPBasicAuth(username, password))
        for item in response.json():
            ids.append(item["id"])

    for id in ids:
        url = "https://www.opencve.io/api/cve/"+id
        response = requests.get(url, auth = HTTPBasicAuth(username, password))
        parsed_data = response.json()
        versionsEndExcluding = []

        # In most cases versionEndExcluding value can be found in cpeMatchs path, at the moment other cases are ommited,
        # cpeMatchs path works for mongodb and postgresql, need to specify bit different path for mysql
        try:
            cpeMatchs = parsed_data['raw_nvd_data']['configurations']['nodes'][0]['cpe_match'][:]
            for record in cpeMatchs:
                versionsEndExcluding.append(record['versionEndExcluding'])
        except Exception:
            pass

        # elif is for postgresql cases since version 10+ (versioning changed to "major.minor" without 3rd value (patch))
        for version in versionsEndExcluding:
            version = version.split(".")
            if len(checkVersion) == len(version):
                if len(version) == 3 and version[:2] == checkVersion[:2] and int(version[2]) > int(checkVersion[2]):
                    numberOfVulnerabilities += 1
                elif  len(version) == 2 and version[0] == checkVersion[0] and int(version[1]) > int(checkVersion[1]):
                    numberOfVulnerabilities += 1

    return numberOfVulnerabilities

print(countDatabaseVulnerabilities(mongoUrl, mongodbVersion))
# To implement:
# compare with numer of vulnerabilities in higher minor version