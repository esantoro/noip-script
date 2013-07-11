#!/usr/bin/python

import time
import urllib
import sys

"""
GET /nic/update?hostname=mytest.testdomain.com&myip=1.2.3.4 HTTP/1.0
Host: dynupdate.no-ip.com
Authorization: Basic base64-encoded-auth-string
User-Agent: Bobs Update Client WindowsXP/1.2 bob@somedomain.com
"""

now  = time.localtime(time.time())

ip_urls = ["http://api.externalip.net/ip/", "http://santoro.tk/ip.php"]

username = "username"
password = "password"

current_ip = None
for url in ip_urls :
	try :
		current_ip = urllib.urlopen(url).read()
		break
	except :
		print "Failed to query {wurl} - {day}/{month}/{year} - {hour}:{minutes}".format(
			day=now[2], month=now[1], year=now[0], hour=now[3], minutes=now[4],
			wurl=url)

if current_ip == None :
	print "Could not fetch ip current ip address - {day}/{month}/{year} - {hour}:{minutes}".format(
		day=now[2], month=now[1], year=now[0], hour=now[3], minutes=now[4])
	sys.exit(1)

HttpAuthToken = "%s:%s" % (username,password)

UpdateUrl = "http://" + HttpAuthToken + "@dynupdate.no-ip.com:80/nic/update?" ;

GetParameters = {"hostname":"ailabs.no-ip.org",
                 "myip":current_ip}

FullUpdateUrl = UpdateUrl + urllib.urlencode(GetParameters)


(response, ip) = urllib.urlopen(FullUpdateUrl).read().split(" ")

print "Result: {result} at {day}/{month}/{year} - {hour}:{minutes}".format(
    result=response, day=now[2], month=now[1], year=now[0], hour=now[3],
    minutes=now[4])


