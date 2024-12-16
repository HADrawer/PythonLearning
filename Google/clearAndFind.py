import gspread
from oauth2client.service_account import ServiceAccountCredentials
import re
scopes = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive',
]

credentials = ServiceAccountCredentials.from_json_keyfile_name("keys.json", scopes)
file = gspread.authorize(credentials)

sheet = file.open("example").sheet1

cell = sheet.find("Hadi")
print(cell)
print("Found something at Row: %s and Column : %s" % (cell.row, cell.col)) 

employess = re.compile(r'(Abas|Sara)')
cell = sheet.findall(employess)
print(cell)

sheet.batch_clear(["A7:C7"])

sheet.clear()