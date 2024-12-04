import os
import shutil

def get_pdf_files(folder_path):
    return [
        os.path.join(folder_path, file_name)
        for file_name in os.listdir(folder_path)
        if os.path.isfile(os.path.join(folder_path, file_name)) and file_name.endswith(".pdf")
    ]

def move_file(file_path, target_folder):
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)
    shutil.move(file_path, os.path.join(target_folder, os.path.basename(file_path)))
