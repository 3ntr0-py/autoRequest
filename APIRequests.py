import requests
import os
from requests.structures import CaseInsensitiveDict

url = "https://api.sep.securitycloud.symantec.com/v1/threat-intel/insight/file/"
print("File: ")
fileH = input()

print("Token: ")
token = "eyJraWQiOiI3b2UxNHBKZVRZU0dqcmJULWVTM01BIiwidHlwIjoiSldUIiwiYWxnIjoiUlMyNTYifQ.eyJzdWIiOiJ7XCJkb21haW5faWRcIjpcImNPTldRWjVXVFVLMVFzQ1RaeEhJemdcIixcIm93bmVyX3VyaVwiOlwiXC92MVwvbWRyXC91c2Vyc1wvMlpBSDhwNVNTUkNmblgtRU15NkVBUVwiLFwic2NvcGVcIjpcIlwiLFwicHJpdnNcIjpcInNlc19tYW5hZ2Vfc2hhcmVkX2VuZHBvaW50IGVkcl92aWV3X2luY2lkZW50cyBjcF90YXJnZXRfcG9saWN5IGFlcF9tYW5hZ2VfY29tbWFuZHMgY3BfZWRpdF9hbGxfcG9saWN5IHNlc191cGRhdGVfc2hhcmVkX2VuZHBvaW50IGNwX2RlbGV0ZV9hbGxfcG9saWN5IGNwX3ZpZXdfcG9saWN5IHNlc192aWV3X3NoYXJlZF9lbmRwb2ludCB2aWV3X2V2ZW50c1wiLFwiY3VzdG9tZXJfaWRcIjpcIktZYXpyR05tUlA2SkNTY0VEa0lKclFcIixcInVyaVwiOlwiXC9vYXV0aDJcL2NsaWVudHNcL08ySUQuS1lhenJHTm1SUDZKQ1NjRURrSUpyUS5jT05XUVo1V1RVSzFRc0NUWnhISXpnLjRmYWp1dmdnNXRldHA2bHJvbmliN3NrNnFcIixcImNsaWVudF9pZFwiOlwiTzJJRC5LWWF6ckdObVJQNkpDU2NFRGtJSnJRLmNPTldRWjVXVFVLMVFzQ1RaeEhJemcuNGZhanV2Z2c1dGV0cDZscm9uaWI3c2s2cVwifSIsInZlciI6MSwiaXNzIjoiaHR0cHM6XC9cL2FwaS5zYWFzLmJyb2FkY29tY2xvdWQuY29tIiwidHR5IjoiYWNjZXNzIiwiZXhwIjoxNjcxNDY5MDA2LCJpYXQiOjE2NzE0NjU0MDYsImp0aSI6IkRWTEJwLTBPUzN1V0gyX2F4ek9NaUEifQ.VbdWGCFm7usaPSc_s2Shz5NsS1Jiw0fkQh5w2dQQMBvmWyNCZcOn9PsMDWt6Ege-6GZhwHBOSLWiJWaZ4bwyOFFbkltr22lTjKTwVW6bgKWrhlM-rosGnpBZR2xaDAAqOI-pPvteb7r3aLJo6fB9jxjl9HqM9OLZ0n7K_ML55MekJpxKwvpymlCOm508F5TgMaYWaGRtRut8nYXLGTLVf1uKuAnmJn9XOZkse30Sem9ZrvYIORR_v15NopWVPtpNvbfmbDtloPkiKki3X4AGMe3re2g2TUTY0d6ABe_5esC7OgYazdV1Z_a0iFSsnGhKu-O5wH3kTmXuadNnSWd4uw"

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