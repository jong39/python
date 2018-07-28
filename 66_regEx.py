import urllib.request
import re  # regular expression

url = "https://www.google.com/googlebooks/uspto-patents-grants-text.html"
html = urllib.request.urlopen(url)
html_content = str(html.read().decode("utf-8"))

# print(html_content)

url_list = re.findall(r"(http)(.+)(zip)", html_content)
for url in url_list:
	print("".join(url))