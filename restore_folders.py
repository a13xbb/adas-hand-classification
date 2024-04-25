import os
from tqdm import tqdm

dir_name = "./DriverMVT_xml/03/"
folder = os.listdir(dir_name)

for pic_name in tqdm(folder):
    if pic_name.endswith('.jpg') or pic_name.endswith('.xml'):
        original_folder_name = pic_name[:pic_name.index('frame') - 1]
        original_pic_name = pic_name[pic_name.index('frame'):]
        os.rename(f'{dir_name}{pic_name}', f'{dir_name}{original_folder_name}/{original_pic_name}')
    # os.rename(f'{dir_name}{pic_name}', f'{dir_name}{pic_name}')