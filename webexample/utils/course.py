from locale import atof, setlocale, LC_NUMERIC
from datetime import date
import requests
import xmltodict

async def get_course():
    setlocale(LC_NUMERIC, 'French_Canada.1252')
    today = date.today().strftime("%d/%m/%Y")
    url = f'https://www.cbr.ru/scripts/XML_dynamic.asp?date_req1={today}&date_req2={today}&VAL_NM_RQ=R01235'
    response = await requests.request("GET", url=url)
    answer = await xmltodict.parse(response.content)
    course = await (atof(answer['ValCurs']['Record']['Value']))
    return course