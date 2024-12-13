# yt-dlpを使用してYouTubeからクリエイティブコモンズの動画をダウンロードするアプリ

import subprocess

path = "exeファイルのパスをここに書く"

command = [
    path,
    "-f", "best",
    "-o", "./video/%(title)s.%(ext)s",
    "youtubeのurlをここに書く"
]

subprocess.run(command)