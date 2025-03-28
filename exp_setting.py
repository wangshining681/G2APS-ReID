import re
import os
import os.path as osp
import shutil

pattern = re.compile(r'([-\d]+)_c(\d)v(\d)')
G2APS_path = 'G2APS-ReID'

query_path = 'query_c0'
gallery_path = 'bounding_box_test_c3'
exp_path = 'exp3_A2G+.txt'
extend_gallery = 'bounding_box_gallery'

with open(osp.join(G2APS_path, exp_path),'w') as f:
    query_list = os.listdir(osp.join(G2APS_path, query_path))
    gallery_list = os.listdir(osp.join(G2APS_path, gallery_path))
    extend_list = os.listdir(osp.join(G2APS_path, extend_gallery))
    
    for pid in query_list:
        pid_path = osp.join(G2APS_path, query_path, pid)
        if osp.isdir(pid_path):
            file_list = os.listdir(pid_path)
            for file in file_list:
                print(osp.join(query_path, pid, file))
                f.writelines(osp.join(query_path, pid, file)+'\n')
    
    for pid in gallery_list:
        pid_path = osp.join(G2APS_path, gallery_path, pid)
        if osp.isdir(pid_path):
            file_list = os.listdir(pid_path)
            for file in file_list:
                print(osp.join(gallery_path, pid, file))
                f.writelines(osp.join(gallery_path, pid, file)+'\n')
    
    for file in extend_list:
        pid, cid, vid = map(int,pattern.search(file).groups())
        if cid != 0:
            print(osp.join(extend_gallery, file))
            f.writelines(osp.join(extend_gallery, file)+'\n')


query_path = 'query_c3'
gallery_path = 'bounding_box_test_c0'
exp_path = 'exp4_G2A+.txt'
extend_gallery = 'bounding_box_gallery'

with open(osp.join(G2APS_path, exp_path),'w') as f:
    query_list = os.listdir(osp.join(G2APS_path, query_path))
    gallery_list = os.listdir(osp.join(G2APS_path, gallery_path))
    extend_list = os.listdir(osp.join(G2APS_path, extend_gallery))
    for pid in query_list:
        pid_path = osp.join(G2APS_path, query_path, pid)
        if osp.isdir(pid_path):
            file_list = os.listdir(pid_path)
            for file in file_list:
                print(osp.join(query_path, pid, file))
                f.writelines(osp.join(query_path, pid, file)+'\n')
    
    for pid in gallery_list:
        pid_path = osp.join(G2APS_path, gallery_path, pid)
        if osp.isdir(pid_path):
            file_list = os.listdir(pid_path)
            for file in file_list:
                print(osp.join(gallery_path, pid, file))
                f.writelines(osp.join(gallery_path, pid, file)+'\n')
    
    for file in extend_list:
        pid, cid, vid = map(int,pattern.search(file).groups())
        if cid != 3:
            print(osp.join(extend_gallery, file))
            f.writelines(osp.join(extend_gallery, file)+'\n')


