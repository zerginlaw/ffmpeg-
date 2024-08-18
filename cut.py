import subprocess

# frame=[6256,14788,18650,28070,37065]#帧frames
# t=[]
# for s in frame:
#     s=s/30
#     t.append(s)
# print(t)
###################################################

t = [207, 491, 620, 934, 1234, 2507]  # 秒数，需要整数,最后一个大于等于视频秒数
source = r"C:\programs\bili\Media\1\out2.mp4"
# source = r"yours.mp4"
out = r"out/output.mp4"
file_name = 'out/list.txt'
#################################################
t_long = None
for ts in t:
    if t_long == None:
        t_long = [ts]
        continue
    t__long = ts - t[(t.index(ts) - 1)]
    t_long.append(t__long)
print(t_long)


def seconds_to_hms(seconds):
    """将秒数转换为时:分:秒格式"""
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60
    return f"{hours:02}:{minutes:02}:{secs:02}"


def cut(start, long, i):
    result = subprocess.run(
        fr'ffmpeg -ss {start} -t {long} -i {source} -copyts -codec copy out\test_video_0{i}_cut.mp4')
    # -ss 在-i 之前可以避免开头有几秒钟静止画面情况，原因可查阅ffmpeg官方文档
    with open(file_name, 'a', encoding='utf-8') as file:
        file.write(f"file test_video_0{i}_cut.mp4\n")
    print(result.returncode)
    print(result.stdout)
    print(result.stderr)


for i in range(len(t)):
    start = t[i - 1] if i > 0 else 0  # second
    start = seconds_to_hms(start)
    long = t_long[i]
    cut(start, long, i)

################################################
# 可以在以下部分打注释运行一遍，在txt中，删除不需要的部分，然后把以上打注释运行一遍拼接
result = subprocess.run(fr'ffmpeg -f concat -i out/list.txt -codec copy {out}')
print(result.returncode)
print(result.stdout)
print(result.stderr)
