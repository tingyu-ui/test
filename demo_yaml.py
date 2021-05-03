#!/usr/bin/env python
# -*- coding:utf-8 -*-
import yaml

print(yaml.load("""
 # - Hesperiidae
 # - Papilionidae
 # - Apatelodidae
 # - Epiplemidae
 a: 1
""", Loader=yaml.FullLoader))
