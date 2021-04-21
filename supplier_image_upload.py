#!/usr/bin/env python3

import os
import requests

url = "http://localhost/upload/"

img_dir = os.path.expanduser("~") + "/supplier-data/images/"
lst_img = os.listdir(img_dir)

jpeg_imgs = [img_name for img_name in lst_img if ".jpeg" in img_name]

for img in jpeg_imgs:
	with open(img_dir + img, "rb") as opened:
		r = requests.post(url, files={"file": opened})
