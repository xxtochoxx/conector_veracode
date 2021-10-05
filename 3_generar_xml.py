import requests
import csv
from veracode_api_signing.plugin_requests import RequestsAuthPluginVeracodeHMAC

VERACODE_API_URL = "https://analysiscenter.veracode.com/api/5.0/"


with open('recursos/build_id_veracode.csv') as File:
        reader = csv.reader(File, delimiter=',')
        for row in reader:
            build_id_veracode = row[1]
            # print("dato "+ build_id_veracode)

            r = requests.post(VERACODE_API_URL + "detailedreport.do", 
                               auth = RequestsAuthPluginVeracodeHMAC(), 
                               data={"build_id" : build_id_veracode})

            data = open('data.xml', 'w')
            data.write(r.text)

        print("Reporte generado !!!")
        print("Fin de la ejecución !!!")