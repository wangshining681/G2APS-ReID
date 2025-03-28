# G2APS-ReID

### Introduction
G2APS-ReID is reconstructed from the G2APS dataset, the copyright belongs to [G2APS](https://github.com/yqc123456/HKD_for_person_search), and the code of the AGPReID dataset from G2APS is open source here for researchers to reconstruct the G2APS-ReID dataset.

### Download G2APS
The G2APS datasets needs to be extracted to /to_path/G2APS/.

Download url:  [https://github.com/yqc123456/HKD_for_person_search](https://github.com/yqc123456/HKD_for_person_search)
### Usage
```Shell
# 1. Cut the ReID data.
python crop_img.py
# 2. Data Split.
python train_test_split.py
# 3. Select query images.
python query_select.py
# 4. Experimental setup.
python exp_setting.py
```



