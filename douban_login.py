# -*- coding:utf8 -*-
import urllib2
string='%E7%99%BB%E5%BD%95'
print urllib2.unquote(string)
from PIL import Image
from StringIO import StringIO

import requests
r = requests.get('http://www.douban.com/accounts/login')
