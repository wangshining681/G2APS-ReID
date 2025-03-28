import os
import os.path as osp
import numpy as np
import scipy.io as scio 
from scipy.io import loadmat
from PIL import Image
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

path = r'G2APS\Image\SSM'
img_mat_path = r'G2APS\annotation\Images.mat'
all_imgs = loadmat(img_mat_path)
all_imgs = all_imgs["Img"].squeeze()
name_to_boxes = {}
name_to_pids = {}
unlabeled_pid = 5555  # default pid for unlabeled people
for img_name, _, boxes in all_imgs:
    img_name = str(img_name[0])
    boxes = np.asarray([b[0] for b in boxes[0]])
    boxes = boxes.reshape(boxes.shape[0], 4)  # (x1, y1, w, h)
    valid_index = np.where((boxes[:, 2] > 0) & (boxes[:, 3] > 0))[0]
    assert valid_index.size > 0, "Warning: {} has no valid boxes.".format(img_name)
    boxes = boxes[valid_index]
    name_to_boxes[img_name] = boxes.astype(np.int32)
    name_to_pids[img_name] = unlabeled_pid * np.ones(boxes.shape[0], dtype=np.int32)

def set_box_pid(boxes, box, pids, pid):
    for i in range(boxes.shape[0]):
        if np.all(boxes[i] == box):
            pids[i] = pid
            return


train = loadmat(r"G2APS\annotation\Person.mat")
train = train["Person"].squeeze()
for index, item in enumerate(train):
    scenes = item[2].squeeze()
    for img_name, box, _ in scenes:
        img_name = str(img_name[0])
        box = box.squeeze().astype(np.int32)
        set_box_pid(name_to_boxes[img_name], box, name_to_pids[img_name], index + 1)


all_imgs = loadmat(osp.join("G2APS", "annotation", "Images.mat"))
all_imgs = all_imgs["Img"].squeeze()
all_imgs = [str(a[0][0]) for a in all_imgs]
crop_path = './crop_img_person/'
if not osp.exists(crop_path):
    os.mkdir(crop_path)

for img_name in all_imgs:
    boxes = name_to_boxes[img_name].copy() 

    boxes[:, 2:] += boxes[:, :2]  # (x1, y1, w, h) -> (x1, y1, x2, y2)
    pids = name_to_pids[img_name]
    cam, height, frame = str(img_name).split('.')[0].split('_')
    if cam[0] == 'S':
        cam_id = 3
    elif cam[0] == 'D':
        cam_id = 0
    squence = int(cam[1])
    img = Image.open(osp.join(path, img_name))
    
    for i in range(0, len(pids)):
        # print(pids[i],boxes[i])
        new_name = "{:04d}_c{:1d}v{:1d}_{:06d}.jpg".format(int(pids[i]), cam_id, squence, int(frame))
        print(new_name)
        if not osp.exists(osp.join(crop_path,str(pids[i]))):
            os.mkdir(osp.join(crop_path, str(pids[i])))
        # print(boxes[i][0],boxes[i][1], boxes[i][2],boxes[i][3])
        cropped = img.crop((boxes[i][0],boxes[i][1], boxes[i][2],boxes[i][3]))
        if not os.path.exists(osp.join(crop_path, new_name)):
            cropped.save(osp.join(crop_path, str(pids[i]), new_name))
        
