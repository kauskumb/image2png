# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import os, sys
from PIL import Image


image_path = sys.argv[1]
new_path = sys.argv[2]

if not os.path.exists(new_path):
    os.makedirs(new_path)
    
for filename in os.listdir(image_path):
    clean_name = os.path.splitext(filename)[0]
    second_name = os.path.splitext(filename)[1]
    if( '.ini' != second_name):
        img = Image.open(f'{image_path}{filename}')
        img.save(f'{new_path}/{clean_name}.png','png')
        print('all done')
    

    