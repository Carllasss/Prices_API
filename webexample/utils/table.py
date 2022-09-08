import httplib2
from oauth2client.service_account import ServiceAccountCredentials
import os
from googleapiclient.discovery import build


sheet_id = '1hmTUTWuEnhoO5VmZLjT-kHN2dbPuIV5ij2Nx6j7K-hI'

def get_table(sheet_id):
    resp = get_service_sacc().spreadsheets().values().get(spreadsheetId=sheet_id, range="A1:Z999").execute()
    return resp['values'][1::]


def get_service_sacc():
    creds_json = os.path.dirname(__file__) + "/resc.json"
    scopes = ['https://www.googleapis.com/auth/spreadsheets']

    creds_service = ServiceAccountCredentials.from_json_keyfile_name(creds_json, scopes).authorize(httplib2.Http())
    return build('sheets', 'v4', http=creds_service)










