#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import pandas as pd
import requests
from io import StringIO
import numpy as np



base_path = '/Users/yangjingxi/Desktop/Paulson/MSS_Wechat'

# Web Scrap Articles from Wechat

# Text Analysis

import cntext as ct
help(ct)

file_path = os.path.join(base_path, 'Dec18.txt')

with open(file_path, 'r', encoding='utf-8') as file:
    content = file.read()


ct.term_freq(content, lang='chinese')
