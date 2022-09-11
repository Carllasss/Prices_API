from pathlib import Path
import httplib2
from oauth2client.service_account import ServiceAccountCredentials
from googleapiclient.discovery import build
import environ
import os

env = environ.Env(
    DEBUG=(bool, False)
)

BASE_DIR = Path(__file__).resolve().parent.parent
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

sheet_id = os.environ.get('SHEET_ID')

def get_id_list(table):
    """Gets the list of IDs from the table"""
    res = []
    for i in table:
        res.append(i[1])
    return res


def get_table(sheet_id):
    """Gets a list of lines from Google sheet"""
    resp = get_service_sacc().spreadsheets().values().get(spreadsheetId=sheet_id, range="A1:Z999").execute()
    return resp['values'][1::]


def get_service_sacc():
    """Gets access to the table through a Google Cloud service account"""
    creds_json = os.path.dirname(__file__) + "/resc.json"
    scopes = ['https://www.googleapis.com/auth/spreadsheets']

    creds_service = ServiceAccountCredentials.from_json_keyfile_name(creds_json, scopes).authorize(httplib2.Http())
    return build('sheets', 'v4', http=creds_service)










