#!/usr/bin/env python
import urllib
from lxml import html
doc = html.fromstring(str(urllib.urlopen("http://vtr.aec.gov.au/HouseDownloadsMenu-15508-csv.htm").read()))

z = [x.attrib['href'] for x in doc.xpath("//a[@href]") if x.text != None and "CSV" in str(x.text.encode("utf-8","ignore")).upper() ]
for i in z:
	url = "http://vtr.aec.gov.au/" + i
	print url
	last_slash = i.rfind("/")
	file = str(i[last_slash+1:])
	file = file.replace("..", "").replace("Downloads/", "").replace("/", "")
	print file
	urllib.urlretrieve(url, file)

