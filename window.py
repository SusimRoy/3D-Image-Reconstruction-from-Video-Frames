from keyframe import extract_keyframes
import os
import itertools
from world import accept

vid_path = ''
folder_path = './vid_frames'
n_frames = extract_keyframes(vid_path, folder_path, 100)
window_size = 5

image_arr = []
for img in os.listdir(folder_path):
    i=0
    while i < window_size:
        image_arr.append(img)
        i+=1
    pair_order_list = itertools.combinations(image_arr,2)
    for i in range(len(pair_order_list)):
        wc_b = accept(pair_order_list[i][0], pair_order_list[i][1])
        
