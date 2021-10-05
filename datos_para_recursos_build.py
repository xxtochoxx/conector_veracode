import sys
import requests
import urllib.request
from veracode_api_signing.plugin_requests import RequestsAuthPluginVeracodeHMAC

VERACODE_API_URL = "https://analysiscenter.veracode.com/api/5.0/"

if __name__ == "__main__":

    result = requests.post(VERACODE_API_URL + "getbuildinfo.do", 
                           auth = RequestsAuthPluginVeracodeHMAC(), 
                           data={"app_id" : "1169095"}) #agregar manualmente el id 

    print(result.text)

    # print(result.status_code)

    #app_id hasta la fecha 17 de Mayo
# app_id="966380" app_name="ach-fulfillment
# app_id="966381" app_name="bank-guarantee
# app_id="966383" app_name="citizens
# app_id="966384" app_name="correspondence
# app_id="966385" app_name="credit-charge-card
# app_id="966386" app_name="credit-facility
# app_id="966387" app_name="currency-exchange
# app_id="966388" app_name="customer-agreement
# app_id="966389" app_name="customer-credit-rating
# app_id="1063942" app_name="customer-identification
# app_id="1063943" app_name="customer-managment
# app_id="1063944" app_name="customer-onboarding
# app_id="966390" app_name="customer-position
# app_id="1063945" app_name="customer-surveys
# app_id="1063946" app_name="document-services
# app_id="1063947" app_name="geolocation
# app_id="955430" app_name="jch-mbbk-bill-payment
# app_id="949564" app_name="jch-mbbk-data-retrieve
# app_id="955431" app_name="jch-mbbk-preference-security
# app_id="955432" app_name="jch-mbbk-transactions
# app_id="1121218" app_name="jch-mbbk-virtual-keyboards
# app_id="1112061" app_name="jch-mdys-moodys-creditlens
# app_id="926305" app_name="jch-slfc-guarantee-overview
# app_id="954491" app_name="jch-slfc-organisation-consulting
# app_id="954492" app_name="jch-slfc-organisation-evaluation
# app_id="954493" app_name="jch-slfc-transaction-management
# app_id="966382" app_name="jsc-cross-bill-payment-processor
# app_id="1074037" app_name="jsc-cross-job-manage
# app_id="966397" app_name="jsc-cross-service-specification
# app_id="966400" app_name="jsc-cross-user-securit
# app_id="966401" app_name="jsc-cross-wu-provider
# app_id="955433" app_name="jsc-mbbk-user-preference
# app_id="954490" app_name="jsc-slfc-organisation-common
# app_id="966391" app_name="loan
# app_id="910027" app_name="mockup-reactive-devsecop
# app_id="966392" app_name="party-authentication
# app_id="966393" app_name="party-data-management
# app_id="966394" app_name="payment-execution
# app_id="966395" app_name="personal-account
# app_id="1063949" app_name="personal-account-v2
# app_id="966396" app_name="product-service
# app_id="1063950" app_name="protection-user-access
# app_id="966398" app_name="transaction-authorization
# app_id="966399" app_name="underwriting
# app_id="1088764" app_name="vd-mf-savings-accounts
# app_id="1088763" app_name="vd-mf-steps
# app_id="1088762" app_name="vd-shell
# app_id="1088765" app_name="vd-ui-webcomponents
    #app_id hasta la fecha 24 de Junio
#app_id="1169098" app_name="jch-ebpm-authorization
#app_id="1169095" app_name="jch-ebpm-customer-signature
#app_id="1169097" app_name="jch-ebpm-personal-loans
#app_id="1169096" app_name="jch-ebpm-preference-settings
#app_id="1169102" app_name="jsc-ebpm-bpm-flow
#app_id="1169100" app_name="jsc-ebpm-bpm-inbox
#app_id="1169101" app_name="jsc-ebpm-customer-offer
#app_id="1169099" app_name="jsc-ebpm-expedient
#app_id="1169104" app_name="jsc-ebpm-parameter-settings