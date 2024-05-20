import os
import pandas as pd
import xml.etree.ElementTree as et
from tqdm import tqdm
import re

dir_name = "./hagrid/"
folder = os.listdir(dir_name)
data = []

for file_name in tqdm(folder):
    if file_name.endswith('.aml'):
        img_path = f'{file_name[:-4]}.jpg'
        
        with open(os.path.join(dir_name, file_name), 'r') as f:
            lines = [line.rstrip().lstrip() for line in f]
            # print(lines)
            for line in lines:
                if line.startswith('<FrameWidth>'):
                    frame_width = re.findall(r'\d+', line)[0]
                elif line.startswith('<FrameHeight>'):
                    frame_height = re.findall(r'\d+', line)[0]
                elif line.startswith('<Object ID'):
                    xywh = re.findall(r'\d+', line)
                    X = xywh[-4]
                    Y = xywh[-3]
                    width = xywh[-2]
                    height = xywh[-1]
            
            # print(xywh)
            
            data.append({'path': img_path,
                        'frame_width': frame_width,
                        'frame_height': frame_height,
                        'class': 'Hand_empty',
                        'X': X,
                        'Y': Y,
                        'width': width,
                        'height': height})
            
annotations = pd.DataFrame(data)
annotations.to_csv('hagrid_annotations.csv', index=False)
        