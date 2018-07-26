import random

print(random.randint(1, 1000))

import time 
print(time.localtime())

import urllib.request

r = urllib.request.urlopen("https://www.rainmaker.com")
print(r.read())
