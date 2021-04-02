import os
from os import listdir
from os.path import isfile, join
from xml.dom import minidom
home = os.path.expanduser("~")
mypath=home+'/.local/share/bijiben'

onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

for file in onlyfiles:
	fullfile = os.path.abspath(os.path.join(mypath, file))
	mydoc = minidom.parse(fullfile)
	title = mydoc.getElementsByTagName('title')[0]
	items = mydoc.getElementsByTagName('body')
	nextitems = mydoc.getElementsByTagName('div')
	print(title.firstChild.data)
	for elem in items:
	    print('* ', elem.firstChild.data)
	for elem in nextitems:
	    print('* ', elem.firstChild.data)
