import time
from datetime import datetime as dt

print(dt.now())
hosts_temp = 'host'
hosts_path =r'c:\Windows\System32\drivers\etc\hosts'
redirect = '127.0.0.1'
sites_that_kill_me = ['www.abc.com', 'abc.com', 'https://abc.go.com']

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 16) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 17):
        print('Working Hours:')
        with open(hosts_path, 'r+') as file:
            content = file.read()
            for site in sites_that_kill_me:
                if site in content:
                    pass
                else:
                    file.write(redirect+ ' '+site+'\n')
    else:
        with open(hosts_path, 'r+') as file:
            content = file.readline()
            file.seek(0)
            for line in content:
                if not any(site in line for site in sites_that_kill_me):
                    file.write(line)
            file.truncate()
        print('Time to play')
    time.sleep(2)


