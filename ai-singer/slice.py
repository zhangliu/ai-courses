# 移除视频开头和结尾的部分
import os;
import re;

ffmpeg_path = os.path.abspath(f"{os.path.dirname(__file__)}/../tools/ffmpeg")
ffprobe_path = os.path.abspath(f"{os.path.dirname(__file__)}/../tools/ffprobe")

# 指定文件夹路径
input_path = f"{os.path.dirname(__file__)}/assets/trim/"
output_path = f'{os.path.dirname(__file__)}/assets/slice/'

# 获取文件夹下所有的文件名
file_list = list(filter(lambda item: re.match('.*\.mp3$', item), os.listdir(input_path)))
file_list.sort()
# file_list = [file_list[0]]

for file_name in file_list:
    input_file = os.path.join(input_path, file_name)
    output_file = os.path.join(output_path, file_name)

    print(f'start handle {file_name} ...')
    os.system(f'ffmpeg -y -i {input_file} -f segment -segment_time 15 -c copy {output_file}.%03d.wav')
