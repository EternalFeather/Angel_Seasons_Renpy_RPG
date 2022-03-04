import os
import cv2
import shutil
import argparse
import numpy as np
import pandas as pd
from pypinyin import pinyin, Style

parser = argparse.ArgumentParser()

parser.add_argument("--f", required=True, type=str, help="input filepath")
args = parser.parse_args()
file_path = args.f

# get_ratio_name
ori_path, ratio_path = "/".join(file_path.split('/')[:-1]), file_path.split('/')[-1]
ratio_name = "".join([i[0] for i in pinyin(ratio_path, style=Style.FIRST_LETTER)])

# calculate_ratio
ratio_map = {}
df = pd.read_csv(ori_path + '/note.csv', engine="python")
df = df[df['body'].str.contains(ratio_name)]

body_files = os.listdir(file_path + '/body')
body_imgs = []
for i, (bf, value) in enumerate(zip(body_files, df['size'].values)):
    img = cv2.imdecode(np.fromfile(file_path + '/body/' + bf, dtype=np.uint8), -1)
    body_imgs.append(img)
    height = img.shape[0]
    ratio_map[bf] = value / height

# change body size
for img_name, img in zip(body_files, body_imgs):
    height = int(round(img.shape[0] * ratio_map[img_name]))
    width = int(round(img.shape[1] * ratio_map[img_name]))
    img = cv2.resize(img, (width, height))
    cv2.imencode('.png', img,)[1].tofile(file_path + '/body/' + img_name)

# change fa size
fa_files = os.listdir(file_path + '/fa')
for name in fa_files:
    ratio = ratio_map["".join([name.split('_')[0], "." + name.split('.')[1]])]
    img = cv2.imdecode(np.fromfile(file_path + '/fa/' + name, dtype=np.uint8), -1)
    height = int(round(img.shape[0] * ratio))
    width = int(round(img.shape[1] * ratio))
    img = cv2.resize(img, (width, height))
    cv2.imencode('.png', img,)[1].tofile(file_path + '/fa/' + name)

# make half body
if not os.path.exists(ori_path + '/half/'):
    os.makedirs(ori_path + '/half/')
    
half_path = ori_path + '/half/' + ratio_path

if not os.path.exists(half_path):
    shutil.copytree(file_path, half_path)

def make_half(img):
    height = int(round(img.shape[0] / 2))
    width = int(round(img.shape[1] / 2))
    img = cv2.resize(img, (width, height))
    return img

body_files = os.listdir(half_path + '/body')
for file in body_files:
    img = cv2.imdecode(np.fromfile(half_path + '/body/' + file, dtype=np.uint8), -1)
    img = make_half(img)
    cv2.imencode('.png', img,)[1].tofile(half_path + '/body/' + file)

# make half fa
fa_files = os.listdir(half_path + '/fa')
for file in fa_files:
    img = cv2.imdecode(np.fromfile(half_path + '/fa/' + file, dtype=np.uint8), -1)
    img = make_half(img)
    cv2.imencode('.png', img,)[1].tofile(half_path + '/fa/' + file)

