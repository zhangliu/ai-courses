import os
import shutil

# 指定文件夹路径
folder_path = f"{os.path.dirname(__file__)}/assets/mp3/"

# 获取文件夹下所有的文件名
file_list = os.listdir(folder_path)

# 遍历文件名,进行重命名操作
for file_name in file_list:
    # 定义新文件名
    new_name = 'new_' + file_name
    
    # 拼接完整文件路径
    old_file_path = os.path.join(folder_path, file_name)
    new_file_path = os.path.join(folder_path, new_name)
    
    print(new_name)
    # 重命名
    # shutil.move(old_file_path, new_file_path)