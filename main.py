# Чи працює код - не знаю.
# Стрьомно на робочому компі запускати )))))


import os
import shutil
import re
import sys


def normalize(filename):

    #транслітерацію
    filename = re.sub(r"[\u0400-\u04FF]", lambda m: chr(m.group(0).lower() + 32), filename)

    # всі символи, крім латинських літер та цифр на '_'
    filename = re.sub(r"[^a-zA-Z0-9_]", "_", filename)

   
    return filename


def process_dir(path):

    path = normalize(path)

    if path in ["archives", "video", "audio", "documents", "images"]:
        return

    for filename in os.listdir(path):

        filename = normalize(filename)

        extension = os.path.splitext(filename)[1]

        file_type = None
        for known_type in ["JPEG", "PNG", "JPG", "SVG", "AVI", "MP4", "MOV", "MKV", "DOC", "DOCX", "TXT", "PDF", "XLSX", "XLS", "PPTX", "MP3", "OGG", "WAV", "AMR", "ZIP", "GZ", "TAR"]:
            if extension == known_type:
                file_type = known_type
                break

        if file_type == "JPEG" or file_type == "PNG" or file_type == "JPG" or file_type == "SVG":

            process_image(os.path.join(path, filename), file_type)
        elif file_type == "AVI" or file_type == "MP4" or file_type == "MOV" or file_type == "MKV":

            process_video(os.path.join(path, filename), file_type)
        elif file_type == "DOC" or file_type == "DOCX" or file_type == "TXT" or file_type == "PDF" or file_type == "XLSX" or file_type == "XLS" or file_type == "PPTX":

            process_document(os.path.join(path, filename), file_type)
        elif file_type == "MP3" or file_type == "OGG" or file_type == "WAV" or file_type == "AMR":

            process_music(os.path.join(path, filename), file_type)
        elif file_type == "ZIP" or file_type == "GZ" or file_type == "TAR":

            process_archive(os.path.join(path, filename), file_type)
        else:
  
            process_unknown(os.path.join(path, filename), file_type)

    for subpath in os.listdir(path):

        if not os.listdir(os.path.join(path, subpath)):

            shutil.rmdir(os.path.join(path, subpath))

        process_dir(os.path.join(path, subpath))

def process_image(path, file_type):

    target_path = os.path.join("images", os.path.basename(path))
    shutil.move(path, target_path)

def process_video(path, file_type):

    target_path = os.path.join("video", os.path.basename(path))
    shutil.move(path, target_path)

def process_document(path, file_type):

    target_path = os.path.join("documents", os.path.basename(path))
    shutil.move(path, target_path)

def process_music(path, file_type):

    target_path = os.path.join("audio", os.path.basename(path))
    shutil.move(path, target_path)

def process_archive(path, file_type):

    target_path = os.path.join("archives", os.path.splitext(os.path.basename(path))[0])
    shutil.unpack_archive(path, target_path)

def process_unknown(path, file_type):

    # Файл залишаємо на місці
    pass

if __name__ == "__main__":

    # target_path = sys.argv[1]
    target_path = f"C:\ТЕСТ\"

    target_path = normalize(target_path)

    os.chdir(target_path)

    process_dir(os.getcwd())

    for path, directories, files in os.walk(os.getcwd()):
       
        if not files and not directories:
            
            shutil.rmdir(path)