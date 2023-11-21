import os
import shutil
import re
import sys
import zipfile
global CYRILLIC_SYMBOLS
global TRANSLATION
CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u","f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")

def normalize(filename):
       # Проводимо транслітерацію кирилиці на латиницю

    # filename = re.sub(r"[\u0400-\u04FF]", lambda m: chr(m.group(0).lower() + 32), filename)
    translated_name = ""

    for c in filename:
        if c in CYRILLIC_SYMBOLS:
            translated_name += TRANSLATION[CYRILLIC_SYMBOLS.find(c)]
        elif c.lower() in CYRILLIC_SYMBOLS:
            
            translated_name += (TRANSLATION[CYRILLIC_SYMBOLS.find(c.lower())]).capitalize()
        else:
            translated_name += c
    
    
    filename = translated_name

    # Замінюємо всі символи, крім латинських літер та цифр, на '_'

    filename = re.sub(r"[^a-zA-Z0-9_:.\\]", "_", filename)

    return filename

def process_folder(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            _, extension = os.path.splitext(file)
            normalized_name = normalize(file)

            if extension.lower() in ['.jpg', '.jpeg', '.png', '.svg']:
                destination = 'images'
            elif extension.lower() in ['.avi', '.mp4', '.mov', '.mkv']:
                destination = 'video'
            elif extension.lower() in ['.doc', '.docx', '.txt', '.pdf', '.xlsx', '.pptx']:
                destination = 'documents'
            elif extension.lower() in ['.mp3', '.ogg', '.wav', '.amr']:
                destination = 'audio'
            elif extension.lower() in ['.zip', '.gz', '.tar']:
                continue
                # destination = 'archives'
                # extract_path = os.path.join(destination, os.path.splitext(normalized_name)[0])
                # with zipfile.ZipFile(file_path, 'r') as zip_ref:
                #     zip_ref.extractall(extract_path)
                # continue
            else:
                continue
                # destination = 'unknown'

            destination_path = os.path.join(destination, normalized_name)
            new_path = os.path.join(folder_path, destination_path)

            up_path = os.path.join(folder_path, destination)

            if not os.path.exists(up_path):
                os.makedirs(up_path)

            shutil.move(file_path, new_path)

    for dir in dirs:
        dir_path = os.path.join(root, dir)
        process_folder(dir_path)

def main():
    # target_folder = input("Введіть шлях до папки для сортування: ")
    target_folder ="C:\\TEST"
    process_folder(target_folder)

if __name__ == "__main__":
    main()