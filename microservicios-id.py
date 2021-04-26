import json
import sys
import requests
from veracode_api_signing.plugin_requests import RequestsAuthPluginVeracodeHMAC

api_base = "https://api.veracode.com/appsec/v1"

if __name__ == "__main__":

    try:
        response = requests.get(api_base + "/applications",
                                auth=RequestsAuthPluginVeracodeHMAC(),
                                params={"size": "500"})
    except requests.RequestException as e:
        print(e)
        sys.exit(1)

    if response.ok:
        print(json.dumps(response.json(), indent=2))
    else:
        print(response.status_code)