import os
import shutil
from tkinter.filedialog import askdirectory

path_folder = askdirectory(title="Select a folder")
try:
    list_archives = os.listdir(path_folder)
except Exception as error:
    print(f"{error}")
    quit()
extensions = {}
for archives in list_archives:
    if "." in archives and archives.rsplit(".")[-1] != "ini":
        extensions.setdefault(archives.rsplit(".",1)[-1], []).append(archives.rsplit(".",1)[0])

for key in extensions:
    if not os.path.exists(f"{path_folder}/{key}"):
        os.makedirs(f"{path_folder}/{key}")

for key in extensions:
    for archive in extensions[key]:
        shutil.move(f"{path_folder}/{archive}.{key}", f"{path_folder}/{key}")