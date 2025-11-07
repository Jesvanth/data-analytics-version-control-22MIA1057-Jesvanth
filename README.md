# AI Prescription Agent

## Overview
**AI Prescription Agent** is an intelligent system designed to automatically read and interpret handwritten medical prescriptions using OCR (Optical Character Recognition) and AI-based text analysis.  
It then logs prescription data to Google Sheets and optionally sends updates or summaries through Telegram.

---

## Features
- **OCR Prescription Reading** — Extracts text from handwritten prescriptions using AI-based OCR.  
- **AI Parser** — Understands and classifies extracted text into medicine names, dosages, and durations.  
- **Google Sheets Logger** — Automatically logs prescription data to connected Google Sheets.  
- **Telegram Integration** — Sends notifications or prescription summaries to Telegram users.  
- **Recommender Module** — Suggests similar medicines or alternatives when recognized text is unclear.

---

## Project Structure
| Folder/File | Description |
|--------------|-------------|
| `main.py` | Entry point of the application. |
| `list_models.py` | Lists and manages available AI models. |
| `test_sheets.py` | Used to test Google Sheets logging functions. |
| `configs/config.yaml` | Configuration settings for OCR, APIs, etc. |
| `configs/credentials.json` | Credentials for Google Sheets API access. |
| `modules/` | Core logic components of the project (OCR, AI parsing, Telegram, logging). |
| `data/samples/` | Example prescription images and logos for testing. |
| `.env` | Environment file storing API keys and credentials (excluded from version control). |
| `requirements.txt` | List of required Python dependencies. |

---

## ⚙️ Installation

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/ai-prescription-agent.git
cd ai-prescription-agent
```

### 2. Create and Activate Virtual Environment
```bash
python -m venv venv
source venv/bin/activate   # on macOS/Linux
venv\Scripts\activate      # on Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Create a `.env` file in the project root:
```ini
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
GOOGLE_SHEET_ID=your_google_sheet_id
OPENAI_API_KEY=your_openai_api_key
```

### 5. Add Credentials
Place your `credentials.json` (Google Sheets API credentials) inside the `configs/` directory.

---

## Running the Application
```bash
python main.py
```

---

## Modules Overview
| Module | Function |
|---------|-----------|
| `ocr_reader.py` | Performs OCR on prescription images. |
| `ai_parser.py` | Extracts and interprets relevant prescription data using NLP. |
| `sheets_logger.py` | Logs processed data to Google Sheets. |
| `telegram_sender.py` | Sends messages/alerts to Telegram users. |
| `recommender.py` | Suggests medicine alternatives or similar products. |
| `utils.py` | Helper functions for data formatting and cleaning. |

---

## Future Improvements
- Integrate multilingual OCR for regional prescriptions.  
- Enhance AI parser with transformer-based models (e.g., GPT or LLaMA).  
- Add voice-based prescription reading and response.  
- Improve UI for doctors and pharmacists.

---

## Author
Developed by **Jesvanth S**  
Contact: jesvanth@gmail.com
