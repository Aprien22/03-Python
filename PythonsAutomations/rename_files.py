import os
import re

def convert_to_snake_case(title):
    """Converts a title to Snake_Case format."""
    title = title.strip()
    words = re.findall(r'[A-Za-z0-9]+', title)  # Extract words/numbers
    return '_'.join(words).capitalize()  # Capitalize first letter & join with '_'

def rename_files_in_folder(folder_path):
    if not os.path.exists(folder_path):
        print("Error: Folder path does not exist.")
        return

    for filename in os.listdir(folder_path):
        name, ext = os.path.splitext(filename)  # Separate name and extension

        # Debugging: Print detected filenames
        print(f"Found file: {filename}")

        # Skip files already in correct format
        if re.match(r"^\[[A-Z]+\]-[A-Za-z0-9_]+$", name):
            print(f"Skipping (Already formatted): {filename}")
            continue

        match = re.match(r"\[(.*?)\](.*)", name)  # Extract bracket text and title
        if match:
            bracket_text, title = match.groups()

            # Convert bracket text to uppercase
            new_bracket_text = bracket_text.upper()

            # Convert title to Snake_Case
            title_snake_case = convert_to_snake_case(title)

            # Construct new filename
            new_filename = f"[{new_bracket_text}]-{title_snake_case}{ext}"

            # Debugging: Print before renaming
            print(f"Renaming: {filename} → {new_filename}")

            # Rename file only if it's different
            old_path = os.path.join(folder_path, filename)
            new_path = os.path.join(folder_path, new_filename)

            try:
                os.rename(old_path, new_path)
                print(f"✔ Renamed: {filename} → {new_filename}")
            except Exception as e:
                print(f"❌ Error renaming {filename}: {e}")

if __name__ == "__main__":
    folder_path = input("Enter the folder path: ").strip('"')
    rename_files_in_folder(folder_path)
