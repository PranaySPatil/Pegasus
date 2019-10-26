import os
import xml.etree.ElementTree as xml
from urlparse import urlparse
from pyunpack import Archive
import random

source_folder_path = ""
source_meta_path =os.path.abspath("Stage1//Stage1_data//Sites.xml")
zip_files_path_prefix = "Stage1//Stage1_data//"
file_extension = ".7z"
data_destination_directory = "Stage2//Stage2_data//"
domains = []
zip_file_paths = []

context = xml.iterparse(source_meta_path, events=("start", "end"))
context = iter(context)
event, root = context.next()
for event, elem in context:
    if event == "end":
        if elem.attrib.has_key('Url') and "meta." not in elem.attrib['Url']:
            domains.append(elem.attrib['TinyName'])
            zip_file_paths.append(urlparse(elem.attrib['Url']).hostname)

# too big for my machine, only trying random 10 sources
domains.remove("stackoverflow")
zip_file_paths.remove("stackoverflow.com")
zip_file_paths = random.sample(zip_file_paths, 10)

for zip_file in zip_file_paths:
    path_to_zip_file = os.path.abspath(zip_files_path_prefix + zip_file + file_extension)
    directory_to_extract_to = os.path.abspath(data_destination_directory + zip_file)
    os.mkdir(directory_to_extract_to)
    Archive(path_to_zip_file).extractall(directory_to_extract_to)