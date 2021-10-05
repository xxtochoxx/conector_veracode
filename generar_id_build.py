import sys
import requests
import urllib.request
from veracode_api_signing.plugin_requests import RequestsAuthPluginVeracodeHMAC

VERACODE_API_URL = "https://analysiscenter.veracode.com/api/5.0/"

if __name__ == "__main__":

    result = requests.post(VERACODE_API_URL + "getapplist.do", 
                           auth = RequestsAuthPluginVeracodeHMAC(), 
                           data={"include_user_info" : "false"})
    print("Generando app id Veracode!!!")
    print(result.text)

    # print(result.status_code)

    print("Fin del proceso!!!")