from keyframe import extract_keyframes
import os
import itertools
from world import accept
from PIL import Image

vid_path = ''
folder_path = './vid_frames'
n_frames = extract_keyframes(vid_path, folder_path, 100)
window_size = 5

image_arr = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.jpg') or f.endswith('.png')]

for i in range(0,image_arr,window_size):
    batch = image_arr[i:i+window_size]
    images = [Image.open(file) for file in batch]
    pair_order_list = itertools.combinations(images,2)
    for i in range(len(pair_order_list)):
        wc_b = accept(pair_order_list[i][0], pair_order_list[i][1])
        
