import gspread
from oauth2client.service_account import ServiceAccountCredentials

scopes = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive',
]

credentials = ServiceAccountCredentials.from_json_keyfile_name("keys.json", scopes)
file = gspread.authorize(credentials)

# new_file = file.create('A new spreadsheet')
# new_file.share('hashemalsaie0442@gmail.com', perm_type='user', role='writer')

new_file = file.open("A new spreadsheet")

worksheet = new_file.add_worksheet(title="Sheet2", rows='100',cols='20')