#!/usr/bin/env python3

import os
import requests

desc_path = os.path.expanduser('~') + '/supplier-data/descriptions/'
list_files = os.listdir(desc_path)

img_path = os.path.expanduser('~') + '/supplier-data/images/'
list_jpeg = [img_name for img_name in os.listdir(img_path) if '.jpeg' in img_name]

list = []

for file in list_files:

	with open(desc_path + file, 'r') as f:
		data = {"name": f.readline().rstrip('\n'),
			"weight": f.readline().rstrip('\n').split()[0],
			"description": f.readline().rstrip('\n')}

	for image in list_jpeg:
		if image.split('.')[0] in file.split('.')[0]:
			data['image_name'] = image

	list.append(data)

for item in list:
	res = requests.post("http://127.0.0.1:80/fruits/",json=item)

	if not res.ok:
		raise Exceptions("POST failed! | Status Code: {} | File: {}".format(response.status_code, f))
