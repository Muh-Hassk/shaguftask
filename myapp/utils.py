import gspread
from oauth2client.service_account import ServiceAccountCredentials
from .models import ShagufTask
from django.conf import settings
import os


def fetch_and_insert_data():
    # Google Sheets API integration
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    
    # JSON KeyFile
    desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
    json_key_path = os.path.join(desktop_path, 'shaguf-413502-dedda8ea0c5f.json')
    
    credentials = ServiceAccountCredentials.from_json_keyfile_name(json_key_path, scope)

    gc = gspread.authorize(credentials)
    sheet = gc.open_by_key('1Q4LDAtA3bQjtnvRAmQ4MZLHYvSLiQ8nCBbwiu5aa3QA').sheet1

    # Clear existing data in the database
    ShagufTask.objects.all().delete()

    # Insert data into the database
    data = sheet.get_all_values()[1:]  # Skip the header row
    for row in data:
        ShagufTask.objects.create(id=row[0], name=row[1], city=row[2], revenue=row[3])

