import os
import pandas as pd
import xml.etree.ElementTree as et
from tqdm import tqdm

dir_name = "./DriverMVT_xml/01/"
folder = os.listdir(dir_name)
data = []
for file_name in tqdm(folder):
    if file_name.endswith('.xml'):
        img_path = f'{file_name[:-4]}.jpg'
        tree = et.parse(os.path.join(dir_name, file_name))
        root = tree.getroot()
        
        size = root.find('size')
        frame_width = size.find('width').text
        frame_height = size.find('height').text
        
        objects = root.findall('object')
        for id, obj in enumerate(objects):
            class_name = obj.find('name').text
            bbox = obj.find('bndbox')
            xmin = float(bbox.find('xmin').text)
            xmax = float(bbox.find('xmax').text)
            ymin = float(bbox.find('ymin').text)
            ymax = float(bbox.find('ymax').text)
            X = xmin
            Y = ymin
            width = round(xmax - xmin, 2)
            height = round(ymax - ymin, 2)
            
            data.append({'path': img_path,
                        'frame_width': frame_width,
                        'frame_height': frame_height,
                        'class': class_name,
                        'X': X,
                        'Y': Y,
                        'width': width,
                        'height': height})
        
annotations = pd.DataFrame(data)
annotations.to_csv('annotations.csv', index=False)
        