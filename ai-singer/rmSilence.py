import ffmpeg;
import os;
import re;
import sys;

ffmpeg_path = os.path.abspath(f"{os.path.dirname(__file__)}/../tools/ffmpeg")
ffprobe_path = os.path.abspath(f"{os.path.dirname(__file__)}/../tools/ffprobe")

sys.path.append(ffmpeg_path)
sys.path.append(ffprobe_path)

def shell(command):
    if (os.system(command) != 0): exit(1)

# 指定文件夹路径
folder_path = f"{os.path.dirname(__file__)}/assets/vocal/"
outputPath = f'{os.path.dirname(__file__)}/assets/trim/'

# 获取文件夹下所有的文件名
file_list = list(filter(lambda item: re.match('.*\.wav$', item), os.listdir(folder_path)))
file_list = [file_list[1]]

for file_name in file_list:
    input_file = os.path.join(folder_path, file_name)
    output_file = os.path.join(outputPath, file_name)
    if (os.path.exists(output_file)): os.remove(output_file)

    # stream = ffmpeg.input(input_file)
    # stream = ffmpeg.filter(stream, 'volumedetect')
    # shell(f'ffmpeg -i {input_file} -af "volumedetect=print_format=json" -f null -')
    shell(f'ffmpeg -y -i {input_file} -af volumedetect,silenceremove=start_periods=1:stop_periods=-1:stop_duration=1:stop_threshold=-20dB {output_file}')
    shell(f'ffmpeg -y -i {output_file} -af volumedetect,silenceremove=start_periods=1:stop_periods=-1:stop_duration=1:stop_threshold=-50dB {output_file}.wav')

    # ffmpeg.output(stream, output_file).run()

    shell(f'ffmpeg -y -i {input_file} -filter_complex "showwavespic=s=640x640" -frames:v 1 {input_file}.png')
    shell(f'ffmpeg -y -i {output_file} -filter_complex "showwavespic=s=640x640" -frames:v 1 {output_file}.png')

    # probe = ffmpeg.probe(output_file)
    # audio = next((stream for stream in probe['streams'] if stream['codec_type'] == 'audio'), None)
    # print(audio, 'xxxxxxxxxxxxxxxxx')
    # max_volume = float(audio['max_volume'])

    # ffmpeg.input(file_path, ss='00:00:10', to='00:00:20').output(outputPath).run()
