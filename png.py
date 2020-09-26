# -*- coding: utf-8 -*-
"""
VS Editor

@author Kaustubh K
 Copyright 2020  Kaustubh K

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
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
    

    