import os 
import shutil
from_dir = "C:/Users/HP/Downloads/C102_assets-main/C102_assets-main"
to_dir = "C:/Users/HP/OneDrive/Desktop/Downloaded images"

list_of_files = os.listdir(from_dir)
print(list_of_files)
# 

for file_name in list_of_files:

    name,extension = os.path.splitext(file_name)
    # print(name)
    # print(extension)

    if extension == '':
        continue
    if extension in ['.txt', '.doc', '.docx', '.pdf']:
        path1 = from_dir + '/' + file_name
        path2 = to_dir + '/' + "Document_files"
        path3 = to_dir + '/' + "Document_files" + '/' + file_name
        print("path1 ",path1)
        print("path3 ",path3)
        if os.path.exists(path2):
            print("moving "+ file_name +  "...")
            # move from path1 to path 3
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print("moving " + file_name + "...")
            shutil.move(path1,path3)