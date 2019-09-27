from os import makedirs
from os import listdir
import shutil
from random import seed
from random import random

dataset_home = 'flowers/'
subdirs = ['train/','test/']
for subdir in subdirs:
    labeldirs = ['daisy/', 'dandelion/', 'rose/', 'sunflower/', 'tulip/']
    for labldir in labeldirs:
        newdir = dataset_home + subdir + labldir
        makedirs(newdir, exist_ok=True)

seed(1)
val_ratio = 0.25
for i in range(5):
    src_directory = current[i]
    for file in listdir(src_directory):
        src = src_directory + '/' + file
        dst_dir = 'train/'
        if random() < val_ratio:
            dst_dir = 'test/'
        dst = dataset_home + dst_dir + names[i] + '/' + file
        shutil.move(src, dst)
