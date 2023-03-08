import ipykernel
import os.path as pt
import os
import fnmatch
from os import path


orginal_path = "E:/ultra star"
list = []
list = os.listdir(orginal_path)

for folder in list:
    new_path = os.listdir("{}/{}".format(orginal_path,folder))
    for file in new_path:
        if file.endswith("txt"):
            new_path = "{}/{}/{}".format(orginal_path, folder, file)
            with open(new_path, "r+") as text_file:
                texts = text_file.read()
                
                texts = texts.replace("Ä™", "e")
                texts = texts.replace("Ä‡", "c")
                texts = texts.replace("Ĺ„", "n")
                texts = texts.replace("Ăł", "o")
                texts = texts.replace("Ä…", "a")
                texts = texts.replace("Ĺ‚", "l")
                texts = texts.replace("Ĺ›", "s")
                texts = texts.replace("Ĺş", "z")
                texts = texts.replace("ĹĽ", "z")
                texts = texts.replace("ę", "e")
                texts = texts.replace("ć", "c")
                texts = texts.replace("ń", "n")
                texts = texts.replace("ó", "o")
                texts = texts.replace("ą", "a")
                texts = texts.replace("ł", "l")
                texts = texts.replace("ś", "s")
                texts = texts.replace("ż", "z")
                texts = texts.replace("ź", "z")
            with open(new_path, "w") as text_file:
                text_file.write(texts)