#!/usr/bin/env python3

import os
import requests

path = os.path.expanduser('~') + '/supplier-data/descriptions/'

for desc in os.listdir(path):
	descriptions = {}
	key = ['','','']
