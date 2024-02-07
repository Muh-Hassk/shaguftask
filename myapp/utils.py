import gspread
from oauth2client.service_account import ServiceAccountCredentials
from .models import ShagufTask
from django.conf import settings
import os

def fetch_and_insert_data():
    try:
        # Google Sheets API integration
        scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
        
        # JSON KeyFile
        desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
        json_key_path = os.path.join(desktop_path, 'shaguf-413502-dedda8ea0c5f.json')
        
        credentials = ServiceAccountCredentials.from_json_keyfile_name(json_key_path, scope)

        gc = gspread.authorize(credentials)
        sheet = gc.open_by_key('1Q4LDAtA3bQjtnvRAmQ4MZLHYvSLiQ8nCBbwiu5aa3QA').sheet1

        sheetData = sheet.get_all_values()

        # Get existing IDs from the database
        existing_ids = list(ShagufTask.objects.values_list('id', flat=True))

        # Insert new data into the database
        data = sheetData[1:]  # Skip the header row
        for row in data:
            # Check if the ID already exists in the database
            if row[0] not in existing_ids:
                # Insert new row into the database
                ShagufTask.objects.create(id=row[0], name=row[1], city=row[2], revenue=row[3])
                # Update existing IDs list
                existing_ids.append(row[0])
    except Exception as e:
        # Handle exceptions
        print(f"An error occurred: {str(e)}")
