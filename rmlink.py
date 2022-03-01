import requests
f = open("url.txt", 'r')
f_new = open("url_ok.txt", 'w')
f_new.seek(0)
f_new.truncate()
line = f.readline()
while line:
    line = line.strip('\n')
    print(line)
    try:
        r = requests.get(line)
        if (r.status_code == 200):
            f_new.write(line + '\n')
    except:
        print("Error on " + line)
    line = f.readline()
