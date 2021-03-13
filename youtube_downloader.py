from pytube import YouTube
from tqdm import tqdm
import os
import subprocess

# add option to choose highest or lowest quality
# fill metadata
# add option to download youtube playlist?
# try if entered url is correct
# add option for video download

print('Welcome to YouTube mp3 downloader.')
print('Do you want to enter urls from text (.txt) file? (One url per line) - y/n ?')

answer = None

while True:
    answer = input()
    if (answer != 'y') and (answer != 'n'):
        print('Wrong input, try again!')
    if (answer == 'y') or (answer == 'n'):
        break

url_list = []

if answer == 'y':
    print('Enter file name with extension (The file needs to be in the same directory)')
    file_name = input()
    f = open(file_name, 'r')

    for line in f:
        url_list.append(line.replace('\n', ''))
elif answer == 'n':
    print('Enter your urls below and when you are done type "exit".')

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

    best_abr = int(video.streams.filter(only_audio=True)[0].abr.replace('kbps', ''))
    best_abr_itag = video.streams.filter(only_audio=True)[0].itag

    for i in range(0, len(video.streams.filter(only_audio=True))):
        current_abr = int(video.streams.filter(only_audio=True)[i].abr.replace('kbps', ''))

        if current_abr > best_abr:
            best_abr = current_abr
            best_abr_itag = video.streams.filter(only_audio=True)[i].itag

    output = video.streams.get_by_itag(best_abr_itag).download(current_path + '\\' + 'Downloads')
   
    os.rename(output, output.replace('.webm', '.mp3'))
