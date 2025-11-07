import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from dotenv import load_dotenv

load_dotenv()

def load_patient_history():
    creds_path = os.getenv("GOOGLE_SHEETS_CREDENTIALS")
    spreadsheet_id = os.getenv("SPREADSHEET_ID")

    if not creds_path or not os.path.exists(creds_path):
        raise ValueError("⚠️ GOOGLE_SHEETS_CREDENTIALS not found in .env or file missing")

    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name(creds_path, scope)
    client = gspread.authorize(creds)
    sheet = client.open_by_key(spreadsheet_id).sheet1
    return sheet.get_all_records()

def generate_recommendations(prescription_summary):
    history = load_patient_history()
    rec = "💡 Recommendations based on prescription and patient history:\n"
    rec += "- Maintain dosage schedule.\n- Drink plenty of fluids.\n- Consult doctor if side effects persist."
    return rec

if __name__ == "__main__":
    sample = "Amoxicillin 500mg for 5 days"
    print(generate_recommendations(sample))
