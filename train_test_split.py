import os
import os.path as osp
import random
from random import randint
import shutil
random.seed(0)

def data_split(full_list, ratio, shuffle=False):
    """
    数据集拆分: 将列表full_list按比例ratio（随机）划分为2个子列表sublist_1与sublist_2
    :param full_list: 数据列表
    :param ratio:     子列表1
    :param shuffle:   子列表2
    :return:
    """
    n_total = len(full_list)
    offset = int(n_total * ratio)
    if n_total == 0 or offset < 1:
        return [], full_list
    if shuffle:
        random.shuffle(full_list)
    sublist_1 = full_list[:offset]
    sublist_2 = full_list[offset:]
    return sublist_1, sublist_2


def get_train_test_id():
    """
    数据集拆分: 将列表full_list按比例ratio（随机）划分为2个子列表sublist_1与sublist_2
    :param full_list: 数据列表
    :param ratio:     子列表1
    :param shuffle:   子列表2
    :return:
    """
    f=open('train_id.txt', encoding='gbk')
    train_id_list = []
    for line in f.readlines():
        train_id_list.append(int(line.strip()))
    print(len(train_id_list))
    f=open('test_id.txt', encoding='gbk')
    test_id_list = []
    for line in f.readlines():
        test_id_list.append(int(line.strip()))
    print(len(test_id_list))
    return train_id_list, test_id_list
    

f=open('info\small_id.txt', encoding='gbk')
small_id_list = []
for line in f.readlines():
    small_id_list.append(int(line.strip()))
len(small_id_list)

f=open('info\large_img_id.txt', encoding='gbk')
large_id_list = []
for line in f.readlines():
    large_id_list.append(int(line.strip()))
len(large_id_list)


path = r'./crop_img_person'
file_list = os.listdir(path)
dist_path = r'./G2APS-ReID/bounding_box_train/'
# 划分训练集和测试集ID
# id_list = [x for x in range(1, 2788)]
# train_id_list, test_id_list = data_split(id_list, 0.5, shuffle=True)
# train_id_list.sort()
# test_id_list.sort()
# train_id_list.extend(small_id_list)
# train_id_list = list(set(train_id_list))
# test_id_list = [x for x in test_id_list if x not in small_id_list]
# print(len(train_id_list))
# print(len(test_id_list))

# train_id_list.extend(large_id_list)
# train_id_list = list(set(train_id_list))
# test_id_list = [x for x in test_id_list if x not in large_id_list]
# print(len(train_id_list))
# print(len(test_id_list))

train_id_list, test_id_list = get_train_test_id()

# 将训练集图片移动到指定文件夹
file_list = os.listdir(path)
dist_path = r'./G2APS-ReID/bounding_box_train'
os.makedirs(dist_path, exist_ok=True)
for file_name in train_id_list:
    file_path = osp.join(path, str(file_name))
    if(not osp.exists(file_path)):
        continue
    print(file_path)
    if(not os.path.exists(osp.join(dist_path, str(file_name)))):
        shutil.move(file_path, dist_path)
dist_path = r'./G2APS-ReID/bounding_box_test_c3'
os.makedirs(dist_path, exist_ok=True)
for file_name in test_id_list:
    file_path = osp.join(path, str(file_name))
    
    if(not osp.exists(file_path)):
        continue
    print(file_path)
    if(not os.path.exists(osp.join(dist_path, str(file_name)))):
        shutil.move(file_path, dist_path)


# 将测试集图片移动到指定文件夹
import re
pattern = re.compile(r'([-\d]+)_c(\d)')

ori_path = r'./G2APS-ReID/bounding_box_test_c3'
dist_path = r'./G2APS-ReID/bounding_box_test_c0'

if not osp.exists(dist_path):
    os.mkdir(dist_path)
file_list = os.listdir(ori_path)
for d1_file in file_list:
    d1_file_path = osp.join(ori_path, d1_file)
    d1_file_list = os.listdir(d1_file_path)
    for d2_file in d1_file_list:
        pid, camid = map(int, pattern.search(d2_file).groups())
        if not osp.exists(osp.join(dist_path, d1_file)):
            os.mkdir(osp.join(dist_path, d1_file))
        file_path = osp.join(d1_file_path, d2_file)
        if camid == 0:
            print(file_path)
            shutil.move(file_path, osp.join(dist_path, d1_file))

# 将扩充数据图片移动到指定文件夹
file_path = osp.join(path,"5555")
shutil.move(file_path, r"G2APS-ReID/bounding_box_gallery")