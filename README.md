# 这是一个剪辑视频的脚本，ffmpeg速度相当快
脚本有注释

## 以下是记录高清修复视频的指令，需要nvenc

### 放大修复视频

nvenc --avhw -i "2.mp4" -c hevc --qvbr 23 --multipass 2pass-full --profile main10 -u P7 --output-depth 10 -b 5 --ref 16 --bref-mode each --lookahead 32 -o "out.mp4" --vpp-resize algo=ngx-vsr,superres-mode=0 --output-res 1920x-2

### 管道模式

nvenc --avhw -i "2.mp4" -c raw --cqp 0 --vpp-resize algo=ngx-vsr,superres-mode=0 --output-res 3840x2160 -o - | nvenc --y4m -c hevc --qvbr 23 --multipass 2pass-full --profile main10 -u P7 --output-depth 10 -b 5 --ref 16 --bref-mode each --lookahead 32 --audio-source "2.mp4:codec=alac" --output-res 1920x1080 --vpp-resize algo=super -o "out2.mp4" -i -

### 更快的管道模式

nvenc --avhw -i "2.mp4" -c avc --lossless --vpp-resize algo=ngx-vsr,superres-mode=0 --output-res 3840x2160 -o - | nvenc --avhw -c hevc --qvbr 23 --multipass 2pass-full --profile main10 -u P7 --output-depth 10 -b 5 --ref 16 --bref-mode each --lookahead 32 --audio-source "2.mp4:codec=alac" --output-res 1920x1080 --vpp-resize algo=super -o "out2.mp4" -i -
