import os
import shutil
import re
import sys
import zipfile
from collections import defaultdict

global CYRILLIC_SYMBOLS
global TRANSLATION

CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u", "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")

def normalize(filename):
    # Проводимо транслітерацію кирилиці на латиницю
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

def process_folder(folder_path, category_counts, known_extensions, unknown_extensions):
    
    for root, dirs, files in os.walk(folder_path):
              
        for file in files:

            file_path = os.path.join(root, file)
            _, extension = os.path.splitext(file)
            normalized_name = normalize(file)

            # if os.path.dirname(file_path) in ["archives", "video", "audio", "documents", "images"]:
            match = re.search(r"(?i)\\(archives|video|audio|documents|images|unknown)\\", file_path)

            if match:
                continue

            if extension.lower() in ['.jpg', '.jpeg', '.png', '.svg']:
                destination = 'images'
            elif extension.lower() in ['.avi', '.mp4', '.mov', '.mkv']:
                destination = 'video'
            elif extension.lower() in ['.doc', '.docx', '.txt', '.pdf', '.xlsx', '.pptx']:
                destination = 'documents'
            elif extension.lower() in ['.mp3', '.ogg', '.wav', '.amr']:
                destination = 'audio'
            elif extension.lower() in ['.zip', '.gz', '.tar']:
                destination = 'archives'
                up_path1 = os.path.join(folder_path, destination)
                if not os.path.exists(up_path1):
                    os.makedirs(up_path1)
                extract_path = os.path.join(destination, os.path.splitext(normalized_name)[0])

                up_path2 = os.path.join(folder_path, extract_path)
                if not os.path.exists(up_path2):
                    os.makedirs(up_path2)
                try:
                    shutil.unpack_archive(file_path, up_path2)
                except Exception:
                    print(f"Achtung! Archive {extract_path} nicht entpackt!")
                try:
                    shutil.move(file_path, up_path2)
                except Exception:
                    a = 0
                known_extensions.add(extension.lower())
                continue
            else:
                destination = 'unknown'
                unknown_folder = os.path.join(folder_path, destination)
                if not os.path.exists(unknown_folder):
                    os.makedirs(unknown_folder)
                destination_path = os.path.join(unknown_folder, normalized_name)
                try:
                    shutil.move(file_path, unknown_folder)
                except Exception:
                    a = 0
                unknown_extensions.add(extension.lower())
                continue

            destination_path = os.path.join(destination, normalized_name)
            new_path = os.path.join(folder_path, destination_path)

            up_path = os.path.join(folder_path, destination)

            if not os.path.exists(up_path):
                os.makedirs(up_path)

            try:
                shutil.move(file_path, new_path)
            except Exception:
                    print(f"Блын! Шо-та пашло не такЪ!")

            category_counts[destination].add(normalized_name)
            known_extensions.add(extension.lower())

    for dir in dirs:
        dir_path = os.path.join(root, dir)
        process_folder(dir_path, category_counts, known_extensions, unknown_extensions)

def remove_empty_folders():
    folder_path = sys.argv[1]
    # folder_path ="\\Users\\Zakharchenko\\Desktop\\Мотлох"

    for root, dirs, files in os.walk(folder_path, topdown=False):
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            if not os.listdir(dir_path):
                os.rmdir(dir_path)

def print_results(category_counts, known_extensions, unknown_extensions):
    print("\nResults:")
    print("Category Counts:")
    for category, count in category_counts.items():
        print(f"{category}: {count}")

    print("\nKnown Extensions:")
    for ext in known_extensions:
        print(ext)

    print("\nUnknown Extensions:")
    for ext in unknown_extensions:
        print(ext)

def main():
 

    target_folder = sys.argv[1]
    # target_folder ="\\Users\\Zakharchenko\\Desktop\\Мотлох"
    # category_counts = defaultdict(str)
    category_counts = defaultdict(set)
    known_extensions = set()
    unknown_extensions = set()

    process_folder(target_folder, category_counts, known_extensions, unknown_extensions)
    remove_empty_folders()
    print_results(category_counts, known_extensions, unknown_extensions)

if __name__ == "__main__":
    main()