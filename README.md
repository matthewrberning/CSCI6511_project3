# CSCI6511_project3
building an adversarial gameplay agent 

import requests

url = "https://www.notexponential.com/aip2pgaming/api/index.php?type=team&teamId=1265"

payload={'': ''}
files=[

]
headers = {
  'x-api-key': '5b3ca1541f18c0dd0120',
  'userid': '1045'
}

response = requests.request("GET", url, headers=headers, data=payload, files=files)

print(response.text)

