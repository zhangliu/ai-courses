# 移除视频开头和结尾的部分
import ffmpeg;
import os;
import re;

# 指定文件夹路径
input_path = f"{os.path.dirname(__file__)}/assets/hxy-mp3/"
output_path = f'{os.path.dirname(__file__)}/assets/trim/'

# 获取文件夹下所有的文件名
file_list = list(filter(lambda item: re.match('.*\.mp3$', item), os.listdir(input_path)))
file_list.sort()
# file_list = [file_list[0]]

for file_name in file_list:
    input_file = os.path.join(input_path, file_name)
    output_file = os.path.join(output_path, file_name)

    probe = ffmpeg.probe(input_file)
    duration = round(float(probe['streams'][0]['duration']))
    end = duration - 5
    print(f'start handle {file_name}， end: {end}...')
    os.system(f'ffmpeg -y -i {input_file} -af atrim=start=50:end={end} {output_file}')
