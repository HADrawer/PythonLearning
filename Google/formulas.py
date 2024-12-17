import gspread
from oauth2client.service_account import ServiceAccountCredentials
scopes = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive',
]

credentials = ServiceAccountCredentials.from_json_keyfile_name("keys.json", scopes)
file = gspread.authorize(credentials)

new_file = file.open("example")

worksheet = new_file.worksheet("الورقة1")

worksheet.update_cell(7,2, "=SUM(B1:B6)")