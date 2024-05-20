import xml.etree.ElementTree as et
from tqdm import tqdm
import os

def get_aml_text(frame_width, frame_height, objs: dict):
    text = f'<IvLog>\n\
    <Parameters>\n\
        <DataSource></DataSource>\n\
        <FramesCount>1</FramesCount>\n\
        <FrameWidth>{frame_width}</FrameWidth>\n\
        <FrameHeight>{frame_height}</FrameHeight>\n\
        <FPS>0.0</FPS>\n\
        <IsMoving>false</IsMoving>\n\
    </Parameters>\n\
    <Frames>\n\
        <Frame ID="1" Timestamp="0" IsGroundTruth="true">\n\
            <Objects>\n'
    for obj in objs:
        text += f'              <Object ID="{obj["ID"]}" Class="{obj["Class"]}" X="{obj["X"]}" Y="{obj["Y"]}" Width="{obj["Width"]}" Height="{obj["Height"]}"/>\n'
        
    text += '            </Objects>\n\
        </Frame>\n\
    </Frames>\n\
</IvLog>'
                            
    return text

dir_name = "./DriverMVT/01/"
folder = os.listdir(dir_name)
for name in folder:
    batch_folder = os.listdir(dir_name + name)
    for file_name in tqdm(batch_folder):
        
        if file_name.endswith('.xml'):
            objs = []

            tree = et.parse(f'{dir_name}{name}/{file_name}')
            root = tree.getroot()

            size = root.find('size')
            frame_width = size.find('width').text
            frame_height = size.find('height').text

            objects = root.findall('object')
            for id, obj in enumerate(objects):
                objs.append({})
                class_name = obj.find('name').text
                bbox = obj.find('bndbox')
                xmin = float(bbox.find('xmin').text)
                xmax = float(bbox.find('xmax').text)
                ymin = float(bbox.find('ymin').text)
                ymax = float(bbox.find('ymax').text)
                X = xmin
                Y = ymax
                width = round(xmax - xmin, 2)
                height = round(ymax - ymin, 2)
                
                objs[-1]['ID'] = id
                objs[-1]['Class'] = class_name
                objs[-1]['X'] = X
                objs[-1]['Y'] = Y
                objs[-1]['Width'] = width
                objs[-1]['Height'] = height
                
            with open(f'{dir_name}{name}/{file_name}', 'w') as f:
                f.write(get_aml_text(frame_width, frame_height, objs))
                
            os.rename(f'{dir_name}{name}/{file_name}', f'{dir_name}{name}/{file_name[:-4]}.aml')
            