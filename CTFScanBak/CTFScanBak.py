# -*- coding:utf-8 -*- 
import requests
import os
import optparse

s = requests.Session()
y = 'y'
n = 'n'

parser = optparse.OptionParser("usage%prog" + "-u <target url>")
parser.add_option('-u', dest = 'tgturl', type = 'string', help = "please scand url.")
(options,args) = parser.parse_args()
tgturl = options.tgturl


if ((tgturl.find("http://")) == -1):
	tgturl = "http://" + tgturl


def get_data(url,haha):
	with open("list.txt","r") as f:
		rainbow = f.read()
		rainbow = rainbow.split("\n")
	for i in rainbow:
		i = i.replace('+',haha)	
		res1 = s.get((url+i)[:-1])
		if (str(res1.status_code) == '200' or str(res1.status_code) =='403' ):
			print "["+str(res1.status_code)+"]"+res1.url
			print "****************"

print "*********************"
middle = tgturl.split("/")
middle1 = str(middle[-1:])[2:-2]
get_data(tgturl[:-len(middle1)],middle1)
