import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

def process_prescription(prescription_text):
    prompt = f"Extract and summarize the following prescription:\n{prescription_text}"
    response = model.generate_content(prompt)
    return response.text

if __name__ == "__main__":
    sample_text = "Patient: John Doe, Medication: Amoxicillin 500mg, Duration: 5 days"
    print(process_prescription(sample_text))
