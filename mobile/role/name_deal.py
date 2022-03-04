import os
import re
import json
from pypinyin import lazy_pinyin
from shutil import copyfile

# maps = {}
maps = json.load(open("name_maps.json", "r"))
root = os.path.abspath(".")

rule = re.compile(r"[0-9a-zA-Z\.\:]+", re.IGNORECASE)

for dirpath, dirnames, filenames in os.walk(root):
    for file in filenames:
        file_path = os.path.join(dirpath, file)
        extensions = os.path.splitext(file_path)[1]

        # 替换中文名
        # new_file_path = file_path.split("\\")
        # for i, n in enumerate(new_file_path):
        #     if not rule.match(n):
        #         new_name = "".join(lazy_pinyin(n))

        #         if new_name in maps and maps[new_name] != n:
        #             print(new_name, n, maps[new_name])

        #         maps[new_name] = n
        #         new_file_path[i] = new_name

        # new_file_path = "\\".join(new_file_path)
        # if new_file_path != file_path:
        #     dir_new_path = "\\".join(new_file_path.split("\\")[:-1])
        #     if not os.path.exists(dir_new_path):
        #         os.makedirs(dir_new_path)
        #     copyfile(file_path, new_file_path)

        # 替换英文成中文
        new_file_path = file_path.split("\\")
        for i, n in enumerate(new_file_path):
        	if n in maps:
        		new_name = maps[n]
        		new_file_path[i] = new_name

        new_file_path = "\\".join(new_file_path)
        
        dir_new_path = "\\".join(new_file_path.split("\\")[:-1])
        if new_file_path != file_path:
	        if not os.path.exists(dir_new_path):
	        	os.makedirs(dir_new_path)
	        copyfile(file_path, new_file_path)

# json.dump(maps, open("name_maps.json", "w"))
