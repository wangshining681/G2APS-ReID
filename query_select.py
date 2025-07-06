import os
import os.path as osp
import numpy as np
import random
import shutil
from sklearn.cluster import KMeans
import cv2
random.seed(0)

c0_path = r'G2APS-ReID/bounding_box_test_c0'
c0_dist_path = r'G2APS-ReID/query_c0'
c3_path = r'G2APS-ReID/bounding_box_test_c3'
c3_dist_path = r'G2APS-ReID/query_c3'
id_list_c0 = os.listdir(c0_path)
id_list_c3 = os.listdir(c3_path)
km_model = KMeans(n_clusters=4 ,n_init= 'auto')
tmp_num = 0

print("Start C0")
for id_ in id_list_c0:
    id_path = osp.join(c0_path, id_)
    dist_id_path = osp.join(c0_dist_path, id_)
    img_X = []
    query_list = [[],[],[],[]]
    query = []
    # tmp_num += 1
    # if tmp_num > 10:
    #     break
    
    os.makedirs(dist_id_path,exist_ok=True)
    print(dist_id_path)
    if osp.isdir(id_path):
        img_list = os.listdir(id_path)
        if len(img_list)<4:
            for img_path in img_list:
                file_path = osp.join(id_path, img_path)
                shutil.copy(file_path, dist_id_path)
            continue
        for img_path in img_list:
            image = cv2.imread(osp.join(id_path, img_path))
            img = cv2.resize(image, (64, 64), interpolation=cv2.INTER_CUBIC)
            #计算图像直方图并存储至X数组
            hist = cv2.calcHist([img], [0, 1], None, [64, 64], [0.0, 255.0, 0.0, 255.0])
            img_X.append(((hist/255).flatten()))
        km_model.fit(img_X)
        y_pred = km_model.predict(img_X) 
        for index, pre in enumerate(y_pred):
            query_list[pre].append(img_list[index])
        for i in range(4):
            file_path = osp.join(id_path, random.choice(query_list[i]))
            shutil.copy(file_path, dist_id_path)
tmp_num = 0
print("Start C3")
for id_ in id_list_c3:
    id_path = osp.join(c3_path, id_)
    dist_id_path = osp.join(c3_dist_path, id_)
    img_X = []
    query_list = [[],[],[],[]]
    query = []
    # tmp_num += 1
    # if tmp_num > 10:
    #     break
    os.makedirs(dist_id_path,exist_ok=True)
    print(dist_id_path)
    if osp.isdir(id_path):
        img_list = os.listdir(id_path)
        if len(img_list)<4:
            for img_path in img_list:
                file_path = osp.join(id_path, img_path)
                shutil.copy(file_path, dist_id_path)
            continue
        for img_path in img_list:
            image = cv2.imread(osp.join(id_path, img_path))
            img = cv2.resize(image, (64, 64), interpolation=cv2.INTER_CUBIC)
            #计算图像直方图并存储至X数组
            hist = cv2.calcHist([img], [0, 1], None, [64, 64], [0.0, 255.0, 0.0, 255.0])
            img_X.append(((hist/255).flatten()))
        km_model.fit(img_X)
        y_pred = km_model.predict(img_X) 
        
        for index, pre in enumerate(y_pred):
            query_list[pre].append(img_list[index])
        
        for i in range(4):
            file_path = osp.join(id_path, random.choice(query_list[i]))
            shutil.copy(file_path, dist_id_path)

