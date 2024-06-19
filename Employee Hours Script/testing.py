import requests

url = "https://2mnext.deltekfirst.com/2MNEXT/api/token"

payload='Username=CCOORAY&Password=Cameron5080!&grant_type=password&Integrated=N&database=C0000004504P_1_2MNEXT00000&Client_Id=d5114b047f724a9d9382384fe37d0937&client_secret=5ecbbf5df9fe4a66a2f55172ad62d285&culture=en-US'
headers = {
  'Content-Type': 'application/x-www-form-urlencoded',
  'Authorization': 'Bearer {{oauth_token}}'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
