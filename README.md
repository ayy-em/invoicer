# Invoice Processor

This script processes invoices stored as PDFs in a folder. It extracts key details using ChatGPT, appends them to a Google Sheet, and moves the processed files to another folder.

# What

1. Takes invoice from folder
2. Sends it to OpenAI API to extract data
3. Sends that data to a google sheet

# How


## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt

## Configure

Create config.py file and set the following variables:

- `FOLDER_PATH`: Path to the folder containing the invoices.
- `PROCESSED_FOLDER`: Path to the folder where processed files will be moved.
- `GOOGLE_CREDENTIALS_PATH`: Path to the Google service account credentials JSON file.
- `GOOGLE_SHEETS_SCOPE`: Scope for accessing Google Sheets.
- `SHEET_ID`: ID of the Google Sheet where data will be appended.

## Run

```bash
python main.py
```

# License

I don't care at all.
