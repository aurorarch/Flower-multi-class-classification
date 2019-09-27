import os
from os import listdir
import numpy as np
from numpy import asarray
from numpy import save
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array

directory=os.listdir('flowers/')
current = []
names = []
for each in directory:
    plt.figure()
    curr = 'flowers/' + each
    names.append(each)
    current.append(curr)
    
photos, labels = list(), list()
for i in range(5):
    folder = current[i]
    
    for file in listdir(folder):
        output = i
        photo = load_img(folder + '/' + file, target_size=(200, 200))
        photo = img_to_array(photo)
        photos.append(photo)
        labels.append(output)
photos = asarray(photos)
labels = asarray(labels)
