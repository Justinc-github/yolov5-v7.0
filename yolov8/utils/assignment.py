import os
import random
import shutil

# 定义源文件夹和三个子文件夹的路径
src_dir = '../images'
dst_dir1 = '../images/train'
dst_dir2 = '../images/valid'

# 创建三个子文件夹
os.makedirs(dst_dir1, exist_ok=True)
os.makedirs(dst_dir2, exist_ok=True)


# 获取源文件夹中所有文件的路径
files = [os.path.join(src_dir, f) for f in os.listdir(src_dir) if os.path.isfile(os.path.join(src_dir, f))]

# 按照7:1:2的比例划分文件
num_files = len(files)
num_files1 = int(num_files * 0.9)
num_files2 = num_files - num_files1


# 随机打乱文件列表
random.shuffle(files)

# 将文件拷贝到三个子文件夹中
for i in range(num_files1):
    shutil.copy(files[i], dst_dir1)

for i in range(num_files1, num_files1 + num_files2):
    shutil.copy(files[i], dst_dir2)
