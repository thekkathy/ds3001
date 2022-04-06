# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 11:19:49 2021

@author: Kathy Kang
"""

import numpy as np
import os

data_path = r'C:\Users\klemb\UVACodingProjects\ds2001\ds2001repo\coffee'
file_name = 'Coffee_TRAIN.txt'
full_path = os.path.join(data_path, file_name)

data = np.loadtxt(full_path)
print(data)