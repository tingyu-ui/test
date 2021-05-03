#!/usr/bin/env python
# -*- coding:utf-8 -*-
import yaml

with open("demo3.yml","w") as f:
    yaml.dump(data={'a': [1,2]}, stream=f)
