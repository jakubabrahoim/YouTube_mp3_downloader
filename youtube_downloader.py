from pytube import YouTube
from tqdm import tqdm
import os
import subprocess

print('Welcome to YouTube mp3 downloader.')
print('Enter your urls below and when you are done type "exit".')

url_list = []

while True:
    url = input()
    if url == 'exit':
        break
    else:
        url_list.append(url)

print('Download in progress.')

for i in tqdm(range(0, len(url_list))):
    video = YouTube(url_list[i])

    current_path = os.path.dirname(os.path.realpath(__file__))
    path_to_mp3 = current_path + '\\' + 'Downloads' + '\\' +  video.title + '.mp3'

    best_abr = int(video.streams.filter(only_audio=True)[0].abr.replace('kbps', ''))
    best_abr_itag = video.streams.filter(only_audio=True)[0].itag

    for i in range(0, len(video.streams.filter(only_audio=True))):
        current_abr = int(video.streams.filter(only_audio=True)[i].abr.replace('kbps', ''))

        if current_abr > best_abr:
            best_abr = current_abr
            best_abr_itag = video.streams.filter(only_audio=True)[i].itag

    output = video.streams.get_by_itag(best_abr_itag).download(current_path + '\\' + 'Downloads' )
    os.rename(output, path_to_mp3)
