import os
from tqdm import tqdm

dir_name = "./hagrid/"
ext = ".aml"

# folder = os.listdir(dir_name)
# for name in folder:
#     inner_folder = os.listdir(dir_name + name)
#     for file_name in inner_folder:
#         if file_name.endswith(ext):
#             os.remove(os.path.join(dir_name+name, file_name))

# dir_name = "./in_car_camera/DriverMVT/1/00d548d7-9de9-4089-b934-6c0d2f0ea3bf"
folder = os.listdir(dir_name)
for file_name in tqdm(folder):
    if file_name.endswith(ext):
        os.remove(os.path.join(dir_name, file_name))