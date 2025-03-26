import openpyxl
from pathlib import Path

EXCEL_PATH = Path("user.xlsx")

def get_user_by_email(email: str):
    wb = openpyxl.load.workbook(EXCEL_PATH)
    sheet = wb.active
    for row in sheet.iter_rows(min_rows=2, values_only=True):
        if row[0]== email:
            return {"email": row[0], "password": row[1]}
    return None