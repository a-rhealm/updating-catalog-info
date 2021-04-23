#!/usr/bin/env python3

import os
import emails
import reports
from datetime import date

desc_path = os.path.expanduser('~') + '/supplier-data/descriptions/'
list_files = os.listdir(desc_path)

report = []

def process_data(data):
	for item in data:
		report.append("name: {}<br/>weight: {}\n".format(item[0], item[1]))
	return report

file_data = []

for file_name in list_files:
	with open(desc_path + file_name, 'r') as f:
		file_data.append([line.strip() for line in f.readlines()])
		f.close()

if __name__ == "__main__":
	summary = process_data(file_data)
	paragraph = "<br/><br/>".join(summary)
	title = "Processed Update on {}\n".format(date.today().strftime("%B, %d, %Y"))
	attachment = "/tmp/processed.pdf"
	reports.generate_report(attachment, title, paragraph)

	subject = "Upload Completed - Online Fruit Store"
	sender = "automation@example.com"
	receiver = "{}@example.com".format(os.environ.get('USER'))
	body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
	message = emails.generate_email(sender, receiver, subject, body, attachment)
	emails.send_email(message)
