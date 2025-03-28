import os
import cv2
import sys
from random import randint
import shutil

#  判断图片是否正常
def is_valid_jpg(jpg_file):
    #  判断jpg文件下载是否完整
    if jpg_file.split('.')[-1].lower() == 'jpg':
        with open(jpg_file, 'rb') as f:
            f.seek(-2, 2)
            return f.read() == b'\xff\xd9'
    else:
        return "this file is not jpg"

#  找出文件夹下所有问题图片，重命名后移动到统一的文件夹，重命名是为了方便后期移动回原位置
def filter_jpg(root_path):
    for package in os.listdir(root_path):  # Cyber
        if package == 'error':  # 不进入error文件夹，这个文件夹单独存放问题图片
            continue
        sub1_path = os.path.join(root_path, package)
        for filename in os.listdir(sub1_path):  # first
            file_path = os.path.join(sub1_path, filename)
            ans = is_valid_jpg(file_path)
            if ans != True:  # 若图片有问题
                newName = package + '_' + str(randint(0, 1000)) + filename
                src = os.path.join(os.path.abspath(sub1_path), filename)
                dst = os.path.join(os.path.abspath(sub1_path), newName)
                try:
                    os.rename(src, dst)  # 重命名
                    shutil.move(dst, os.path.join(root_path, 'error', newName))  # 移动图片
                except:
                    print("falure")
                    sys.exit(0)
                print(sub1_path)
                print(filename)

#  修复问题图片后，保存至ok文件夹(这个文件夹要提前创建)，后面需要手动移动一下修复后的图片
def repair_img(root_path):
    path = os.path.join(root_path, "error")
    _path = os.path.join(root_path, "ok")
    for fileName in os.listdir(path):
        file_path = os.path.join(path, fileName)
        img = cv2.imread(file_path)
        new_path = os.path.join(_path, fileName)
        cv2.imwrite(new_path, img)
        if is_valid_jpg(new_path):  # 新存储的图片是ok的
            os.remove(file_path)


if __name__ == '__main__':
    root_path = "./G2APS/Image"
    filter_jpg(root_path)
    repair_img(root_path)