import requests
import os
from requests.structures import CaseInsensitiveDict

url = "https://api.sep.securitycloud.symantec.com/v1/threat-intel/insight/file/"
print("File: ")
fileH = input()

print("Token: ")
token = input()

with open('results.txt', 'w+') as output:
    with open(fileH, 'r') as file:

        headers = CaseInsensitiveDict()
        headers["Authorization"] = "Bearer " + token

        for i in file:
            item = i.strip()
            ver = url + item
            print(ver)
            resp = requests.get(ver, headers=headers)

            try :
                line = item + "," + str(resp.status_code) + "," + str(resp.reputation) + "\n"
            except AttributeError:
                line = item + "," + str(resp.status_code) + "\n"

            output.write(line)
            print(resp.status_code)
            print(resp.content)

os.system("start results.txt")
