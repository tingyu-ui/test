#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
# r = requests.get("http://www.baidu.com")
r = requests.post("http://httpbin.org/post", data = {'key':'valus'})
print(r.text)
