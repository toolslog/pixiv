# coding=utf-8

import requests
import time
import os
import json

url = 'https://api.lolicon.app/setu/v2'
download_num = 30

def download(num):
    for i in range(0, num):
        r = requests.get(url)
        dic = r.json()

        pic_title = dic["data"][0]["title"]
        pic_url = dic["data"][0]["urls"]["original"]
        pic_pid = dic["data"][0]["pid"]
        pic_author = dic["data"][0]["author"]
        pic_filename = str(pic_pid) + "_" + pic_title + \
            "_" + pic_author + ".png"
        os.system("wget -nv " + pic_url + " -O \"pic/" +
                  pic_filename + "\" --connect-timeout 2 --no-check-certificate --user-agent=\"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0\"")
        time.sleep(1)


def upload_image(filepath):
    try:
        files = {'smfile': open(filepath, 'rb')}
        api = 'https://sm.ms/api/v2/upload'
        res = requests.post(api, files=files).json()
        if res['success']:
            f = open("url.txt", 'a')
            pic_url = res['data']['url']
            print(pic_url)
            data = f.write(pic_url + "\n")
        else:
            print(res['message'])
    except Exception as e:
        print(e)

def del_file(path):
    ls = os.listdir(path)
    for i in ls:
        c_path = os.path.join(path, i)
        if os.path.isdir(c_path):
            del_file(c_path)
        else:
            os.remove(c_path)


os.mkdir('pic')

download(download_num)

pic_path = r'pic/'
pic_name = os.listdir(pic_path)
for filename in os.listdir(pic_path):
    upload_image(pic_path + filename)
    if (download_num > 10):
        time.sleep(3)

del_file(r'pic/')
os.rmdir(r'pic/')
