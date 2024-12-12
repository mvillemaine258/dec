import vlc
import time

def play_m3u8(url):
    # 创建一个VLC实例
    instance = vlc.Instance()

    # 创建一个Media对象
    media = instance.media_new(url)

    # 创建一个Media Player对象
    player = instance.media_player_new()

    # 设置Media Player的Media
    player.set_media(media)

    # 播放
    player.play()

    # 等待视频播放完毕
    while player.get_state() != vlc.State.Ended:
        time.sleep(1)

# 使用你的m3u8链接
url = "https://y1.wuyufei1.cn/20240517/vtmWrGhj/2000kb/hls/index.m3u8"
play_m3u8(url)