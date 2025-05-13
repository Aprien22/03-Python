import os
import PyPDF2
import re

def extract_text_from_pdf(file_path):
    """Extracts the first line of text from a PDF file."""
    try:
        with open(file_path, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            if reader.pages:
                text = reader.pages[0].extract_text()
                if text:
                    return text.split("\n")[0]  # First line as title
    except Exception as e:
        print(f"Error extracting text: {e}")
    return None

def convert_to_snake_case(text):
    """Converts extracted text to a clean Snake_Case format."""
    text = re.sub(r'[^a-zA-Z0-9 ]', '', text)  # Remove special chars
    words = text.split()
    return '_'.join(words).capitalize() if words else "Untitled"

def rename_pdfs(folder_path):
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(".pdf"):
            file_path = os.path.join(folder_path, filename)
            extracted_title = extract_text_from_pdf(file_path)

            if extracted_title:
                new_name = f"{convert_to_snake_case(extracted_title)}.pdf"
                new_path = os.path.join(folder_path, new_name)

                if filename != new_name:
                    try:
                        os.rename(file_path, new_path)
                        print(f"✔ Renamed: {filename} → {new_name}")
                    except Exception as e:
                        print(f"❌ Error renaming {filename}: {e}")
                else:
                    print(f"Skipping (Already renamed): {filename}")

if __name__ == "__main__":
    folder_path = input("Enter the folder path: ").strip('"')
    rename_pdfs(folder_path)
