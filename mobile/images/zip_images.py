from PIL import Image
import cv2
import os

root = os.path.abspath(".")

# 单目录
files = os.listdir(root)
for file in files:
	file_path = os.path.join(root, file)
	ori_name, extensions = os.path.splitext(file_path)

# 全路径
# for dirpath, dirnames, filenames in os.walk(file_dir):  
#     for file in filenames :  
#         if os.path.splitext(file)[1] == '.jpg':  
#             L.append(os.path.join(dirpath, file))  

	if extensions == ".png":
		print(file_path, ori_name)

		# 压缩png成jpg图片
		img = Image.open(file_path)
		img = img.convert("RGB")
		img.save(ori_name + ".png", quality=50)
		# os.remove(file_path)
		
		# 压缩png成png图片
		# img = cv2.imread(file_path, cv2.IMREAD_UNCHANGED)
		# cv2.imwrite(file_path, img, [cv2.IMWRITE_PNG_COMPRESSION, 9])

		