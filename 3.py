#!/usr/bin/python

#demo of requests library

import requests

r = requests.get('http://pramode.net')

print r.content
