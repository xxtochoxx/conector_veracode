import sys
import requests
import json
from veracode_api_signing.plugin_requests import RequestsAuthPluginVeracodeHMAC

#JSON
api_base = "https://api.veracode.com/appsec/v2"
headers = {"User-Agent": "Python HMAC Example",'content-type': 'application/json'}

if __name__ == "__main__":

    try:
        response = requests.get(api_base + "/applications/fa8e1406-c8f4-417f-a973-6f3a17c10e37/summary_report", auth=RequestsAuthPluginVeracodeHMAC(), headers=headers)
        
    except requests.RequestException as e:
        print("Whoops!")
        print(e)
        sys.exit(1)

    if response.ok:
        data = response.json()
        print(data)

        cadena_json = json.dumps(data)

        with open('datos.json','w') as f:

        	json.dump(data, f)

    else:
        print(response.status_code)