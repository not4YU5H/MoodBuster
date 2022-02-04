
import os
os.add_dll_directory(r'C:\\Program Files\\VideoLAN\\VLC')

import vlc
import pafy

url = "https://youtu.be/KIAZWfSmNOU"
video = pafy.new(url)
best = video.getbest()
media = vlc.MediaPlayer(best.url)
media.play()