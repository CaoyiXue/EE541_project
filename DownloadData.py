import requests
import zipfile
import shutil
import os

print('Downloading started')
URL = "https://github.com/CaoyiXue/data/archive/refs/heads/main.zip"

req = requests.get(URL)
filename = "data.zip"

with open(filename,'wb') as output_file:
    output_file.write(req.content)


with zipfile.ZipFile(filename, 'r') as zip_ref:
    zip_ref.extractall("./")

os.remove(filename)

source = "./data-main"
destination = "./data"
shutil.move(source, destination) 

dir_path = "data/__MACOSX"
try:
    shutil.rmtree(dir_path)
except OSError as e:
    pass

print('Downloading Completed')