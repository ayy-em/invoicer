import requests
from config import config as cfg


# Base URL for OpenAI's Files API
OPENAI_FILES_API_URL = "https://api.openai.com/v1/files"
OPENAI_CHAT_API_URL = "https://api.openai.com/v1/chat/completions"

# Upload the file to OpenAI
def upload_file(file_path):
    headers = {
        "Authorization": f"Bearer {cfg.OPENAI_API_KEY}",
        "OpenAI-Organization": cfg.OPENAI_ORG_KEY,
        "OpenAI-Project": cfg.OPENAI_PROJECT_KEY
        }
    with open(file_path, "rb") as file:
        response = requests.post(
            OPENAI_FILES_API_URL,
            headers=headers,
            files={"file": (file_path, file, "application/pdf")},
            data={"purpose": "fine-tune"}
        )
    response.raise_for_status()
    file_data = response.json()
    return file_data["id"]

# Use the file with GPT
def extract_invoice_details(file_id):
    headers = {"Authorization": f"Bearer {cfg.OPENAI_API_KEY}"}
    prompt = (
        "Extract the following details from the invoice uploaded as a file:\n"
        "- Invoice Date (datetime)\n"
        "- Company that issued the invoice (string)\n"
        "- Invoice Amount (float)\n"
        "- VAT (float)\n"
        f"The file ID for this invoice is: {file_id}."
    )
    response = requests.post(
        OPENAI_CHAT_API_URL,
        headers=headers,
        json={
            "model": "gpt-4",
            "messages": [{"role": "user", "content": prompt}]
        }
    )
    response.raise_for_status()
    data = response.json()
    return data["choices"][0]["message"]["content"].strip().split(",")

# Main function to handle file upload and extraction
def process_file(file_path):
    try:
        file_id = upload_file(file_path)
        return extract_invoice_details(file_id)
    except Exception as e:
        raise RuntimeError(f"Error processing file {file_path}: {e}")