from PIL import Image
import cv2
import os
import json

import tinify
tinify.key = "gqx3YVZqL2KPFrsQHMRcqPpDYYdlMkCv"

root = os.path.abspath(".")


# 单目录
# files = os.listdir(root)
# for file in files:
#     file_path = os.path.join(root, file)
#     ori_name, extensions = os.path.splitext(file_path)

# 全路径
name = ""
count = 1
for dirpath, dirnames, filenames in os.walk(root):
    for file in filenames:
        file_path = os.path.join(dirpath, file)
        extensions = os.path.splitext(file_path)[1]

        if extensions == ".png":
            print(file_path)

            if count <= 500:
                try:
                    source = tinify.from_file(file_path)
                    source.to_file(file_path)
                except Exception as e:
                    print(e)
            else:
                break

    if count > 500:
        break


            # 压缩png成jpg图片
            # img = Image.open(file_path)
            # img = img.convert("RGB")
            # img.save(ori_name + ".jpg", "jpeg")
            # os.remove(file_path)
            
            # # 压缩png成png图片
            # img = cv2.imread(file_path, cv2.IMREAD_UNCHANGED)
            # cv2.imwrite(file_path, img, [cv2.IMWRITE_PNG_COMPRESSION, 9])

        