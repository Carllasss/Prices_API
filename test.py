from datetime import date
import requests
import xmltodict

def get_course():
    today = date.today().strftime("%d/%m/%Y")
    url = f'https://www.cbr.ru/scripts/XML_dynamic.asp?date_req1={today}&date_req2={today}&VAL_NM_RQ=R01235'
    response = requests.request("GET", url=url)
    answer = xmltodict.parse(response.content)
    course = float(str(answer['ValCurs']['Record']['Value']).replace(',', '.'))
    return course

print(get_course())