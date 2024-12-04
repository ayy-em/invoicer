from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from config.config import GOOGLE_CREDENTIALS_PATH, GOOGLE_SHEETS_SCOPE, SHEET_ID

def init_sheets_api():
    creds = Credentials.from_service_account_file(GOOGLE_CREDENTIALS_PATH, scopes=GOOGLE_SHEETS_SCOPE)
    print("initialized gsheets")
    return build("sheets", "v4", credentials=creds)

def append_to_sheet(service, row):
    sheet = service.spreadsheets()
    body = {"values": [row]}
    sheet.values().append(
        spreadsheetId=SHEET_ID,
        range="raw_expenses",
        valueInputOption="RAW",
        body=body
    ).execute()
    print(f"Appended to sheet: {str(body)}")
