import ffmpeg;
import os;

# 指定文件夹路径
folder_path = f"{os.path.dirname(__file__)}/assets/mp3/"
outputPath = f'{os.path.dirname(__file__)}/assets/slice/0.mp3'

# 获取文件夹下所有的文件名
file_list = os.listdir(folder_path)
file_list = [file_list[0]]

print(file_list, 'xxxxxxxxxxxxxxxx')

for file_name in file_list:
    file_path = os.path.join(folder_path, file_name)
    ffmpeg.input(file_path, ss='00:00:10', to='00:00:20').output(outputPath).run()
