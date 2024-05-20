import os

dir_name = "./DriverMVT_xml/03/"
folder = os.listdir(dir_name)
for name in folder:
    batch_folder = os.listdir(dir_name + name)
    for file_name in batch_folder:
        os.rename(f'{dir_name}{name}/{file_name}', f'{dir_name}{name}_{file_name}')