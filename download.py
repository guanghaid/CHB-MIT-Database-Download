import os
import sys
from urllib.request import urlopen

def download_big_file(url, target_file_name):

    response = urlopen(url)
    chunk = 16 * 1024
    with open(target_file_name, 'wb') as f:
        while True:
            chunk = response.read(chunk)
            if not chunk:
                break
            f.write(chunk)


result=[]
with open('RECORDS.txt','r') as f:
    for line in f:
        result.append(line.strip('\n').split(','))

current_path = 'D:/code/EEG/epilepsy_detection/'  # change this path to your current path
for fname in result:
    url = 'https://physionet.org/pn6/chbmit/' + fname[0]
    if not os.path.isdir(current_path + fname[0].split('/')[0]):
        os.mkdir(current_path + fname[0].split('/')[0])
    download_big_file(url, fname[0])


