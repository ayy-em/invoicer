import os
from config.config import FOLDER_PATH, PROCESSED_FOLDER
from file_utils import get_pdf_files, move_file
from openai_api import extract_invoice_details
from gsheets import init_sheets_api, append_to_sheet


def process_files():
    service = init_sheets_api()
    pdf_files = get_pdf_files(FOLDER_PATH)

    for file_path in pdf_files:
        print(file_path)
        try:
            details = extract_invoice_details(file_path)
            append_to_sheet(service, details)
            move_file(file_path, PROCESSED_FOLDER)
            print(f"Processed and moved: {os.path.basename(file_path)}")
        except Exception as e:
            print(f"Error processing {os.path.basename(file_path)}: {e}")

if __name__ == "__main__":
    process_files()
