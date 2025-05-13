import os
import re

def revert_filenames(folder_path):
    if not os.path.exists(folder_path):
        print("Error: Folder path does not exist.")
        return

    for filename in os.listdir(folder_path):
        match = re.match(r"\[(.*?)\]-(.*)", filename)  # Extract text inside brackets and title
        if match:
            bracket_text, title = match.groups()

            # Convert bracket text to lowercase
            new_bracket_text = bracket_text.lower()

            # Convert Title_Case_With_Underscores back to PascalCase
            title_formatted = title.replace("_", " ").title().replace(" ", "")

            # Construct new filename
            new_filename = f"[{new_bracket_text}]{title_formatted}"

            # Rename file
            old_path = os.path.join(folder_path, filename)
            new_path = os.path.join(folder_path, new_filename)
            os.rename(old_path, new_path)
            print(f'Reverted: {filename} → {new_filename}')

if __name__ == "__main__":
    folder_path = input("Enter the folder path: ").strip('"')  # Accept user input for folder path
    revert_filenames(folder_path)
