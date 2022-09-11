from locale import atof, setlocale, LC_NUMERIC
from datetime import date, timedelta
import requests
import xmltodict

def get_course():
    today = date.today()
    day = today.strftime("%d/%m/%Y")
    url = f'https://www.cbr.ru/scripts/XML_dynamic.asp?date_req1={day}&date_req2={day}&VAL_NM_RQ=R01235'
    response = requests.request("GET", url=url)
    answer = xmltodict.parse(response.content)
    try:
        course = float(str(answer['ValCurs']['Record']['Value']).replace(',', '.'))
        return course
    except KeyError:
        today = today - timedelta(days=1)
        day = today.strftime("%d/%m/%Y")
        url = f'https://www.cbr.ru/scripts/XML_dynamic.asp?date_req1={day}&date_req2={day}&VAL_NM_RQ=R01235'
        response = requests.request("GET", url=url)
        answer = xmltodict.parse(response.content)
        course = float(str(answer['ValCurs']['Record']['Value']).replace(',', '.'))
        return course