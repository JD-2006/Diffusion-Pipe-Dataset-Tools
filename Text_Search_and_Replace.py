import os

def get_user_input():
    folder = input("Enter the folder path: ").strip()
    word_to_find = input("Enter the word to replace: ").strip()
    replacement_word = input("Enter the new word: ").strip()
    return folder, word_to_find, replacement_word

def replace_words_in_files(folder, target, replacement):
    for root, _, files in os.walk(folder):
        for file in files:
            if file.endswith(".txt"):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()

                    if target in content:
                        content = content.replace(target, replacement)
                        with open(file_path, 'w', encoding='utf-8') as f:
                            f.write(content)
                        print(f"Updated: {file_path}")
                except Exception as e:
                    print(f"Error processing {file_path}: {e}")

if __name__ == "__main__":
    folder_path, find_word, replace_word = get_user_input()
    if os.path.isdir(folder_path):
        replace_words_in_files(folder_path, find_word, replace_word)
    else:
        print("Invalid folder path.")
